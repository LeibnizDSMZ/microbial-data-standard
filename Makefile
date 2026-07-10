# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

ifeq ($(CONTAINER),container)
$(info Makefile enabled, proceeding ...)
else
$(error Error: Makefile disabled, exiting ...)
endif

SHELL := /bin/bash
ROOT_MAKEFILE := $(abspath $(patsubst %/, %, $(dir $(abspath $(lastword $(MAKEFILE_LIST))))))

$(shell $(ROOT_MAKEFILE)/bin/install/env.sh $(ROOT_MAKEFILE)/package.env > .env.mk 2>/dev/null)
-include .env.mk

export
export PATH := $(PATH):$(shell pwd)/$(UV_INSTALL_DIR)/:$(shell pwd)/$(PNPM_HOME)/bin
OLLAMA_MODEL?=qwen3.6:27b-q4_K_M

$(eval UVEL := $(shell which uv && echo "true" || echo ""))
$(eval PNPMEL := $(shell which pnpm && echo "true" || echo ""))
UVE = $(if $(UVEL),uv,$(ROOT_MAKEFILE)/$(UV_INSTALL_DIR)/uv)
PNPME = $(if $(PNPMEL),pnpm,$(ROOT_MAKEFILE)/$(PNPM_HOME)/bin/pnpm)

dev: setupUv setupPnpm
	$(UVE) sync --frozen --all-groups
	find .git/hooks -name "*.old" -delete
	$(UVE) run lefthook uninstall 2>&1 || echo "not installed"
	$(UVE) run lefthook install
	@HOOK_FILE=.git/hooks/pre-push; \
	if ! grep -q "git lfs pre-push" $$HOOK_FILE; then \
		echo "command -v git-lfs >/dev/null && git lfs pre-push \"\$$@\"" >> $$HOOK_FILE; \
		echo "added 'git lfs pre-push' to pre-push hook."; \
	fi

tests: setupUv
	$(UVE) sync --frozen --group test

build: setupUv
	$(UVE) sync --frozen

docs: setupUv setupPnpm
	$(UVE) sync --frozen --group docs

setupUv:
	bash $(ROOT_MAKEFILE)/$(BIN_INSTALL_UV)

setupPnpm:
	bash $(ROOT_MAKEFILE)/$(BIN_INSTALL_PNMP)

unstaged:
	@if ! git diff --quiet --exit-code; then \
		echo "ERROR: Unstaged changes found!"; \
		exit 1; \
	fi
	@echo "No unstaged changes. Proceeding..."

setupDocs: unstaged
	$(UVE) run mds_docs
	$(UVE) run mds_mermaid
	git add .

setupLicense: unstaged
	bash $(BIN_RUN_LICENSE_LINT)
	git add .

RAN := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

runAct:
	@echo "source .venv/bin/activate; rm /tmp/$(RAN)" > /tmp/$(RAN)
	bash --init-file /tmp/$(RAN)

runChecks:
	$(UVE) run lefthook run pre-commit --all-files -f

buildDocs:
	cd $(ROOT_MAKEFILE)/$(PKG_DOCS) && $(PNPME) run build

runDocs: buildDocs
	$(UVE) run zensical build -f $(CONFIG_DOCS)

serveDocs: buildDocs
	$(UVE) run zensical serve -f $(CONFIG_DOCS) -a 0.0.0.0:8000

runTests:
	$(UVE) run tox

runBuild:
	$(UVE) build --package microbial-strain-data-model

runBump: unstaged
	$(UVE) run cz bump --files-only --yes --changelog
	git add .
	$(UVE) run cz version --project | xargs -i git commit -am "bump: release {}"

runLock runUpdate: %: export_%

export_runLock:
	$(UVE) lock
	cd $(PKG_DOCS) && $(PNPME) install --lockfile-only

export_runUpdate:
	$(UVE) lock -U
	cd $(PKG_DOCS) && $(PNPME) update

com commit:
	@echo "" > .commit_msg
	@if curl -sf http://ollama:11434; then \
		$(MAKE) message || exit 1; \
	else \
		$(UVE) run cz commit || exit 1; \
	fi
	@echo "" > .commit_msg

recom recommit:
	@if curl -sf http://ollama:11434; then \
		[ -s .commit_msg ] || (echo "Missing commit message!" && exit 1); \
		git commit -F .commit_msg || exit 1; \
	else\
		$(UVE) run cz commit --retry || exit 1; \
	fi
	@echo "" > .commit_msg

message:
	git diff --staged -- . ':(exclude)uv.lock' ':(exclude)*pnpm-lock.yaml' | \
		jq -Rs --rawfile prompt configs/prompt/commit.md \
			'{"stream": false, "model": "$(OLLAMA_MODEL)", "prompt": ("<GIT_DIFF>" + . + "</GIT_DIFF>" + $$prompt)}' | \
		curl -s -X POST http://ollama:11434/api/generate \
			-H "Content-Type: application/json" \
			-d @- | \
		jq -r 'select(.done == true) | .response' > .commit_msg
	vim .commit_msg
	@if ! $(UVE) run cz check --commit-msg-file .commit_msg; then \
		echo "Commit message failed cz check. Aborting."; \
		echo "" > .commit_msg; \
		exit 1; \
	fi
	git commit -F .commit_msg

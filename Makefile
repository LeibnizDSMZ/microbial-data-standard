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
export PATH := $(PATH):$(shell pwd)/$(UV_INSTALL_DIR)
OLLAMA_MODEL?=qwen3.6:27b-q4_K_M

$(eval UVEL := $(shell which uv && echo "true" || echo ""))
UVE = $(if $(UVEL),uv,$(UV_INSTALL_DIR)/uv)

dev: setup
	$(UVE) sync --frozen --all-groups
	$(UVE) run lefthook uninstall 2>&1 || echo "not installed"
	$(UVE) run lefthook install
	@HOOK_FILE=.git/hooks/pre-push; \
	if ! grep -q "git lfs pre-push" $$HOOK_FILE; then \
		echo "command -v git-lfs >/dev/null && git lfs pre-push \"\$$@\"" >> $$HOOK_FILE; \
		echo "added 'git lfs pre-push' to pre-push hook."; \
	fi

tests: setup
	$(UVE) sync --frozen --group test

build: setup
	$(UVE) sync --frozen

docs: setup
	$(UVE) sync --frozen --group docs

setup:
	which uv || [ -d "${UV_INSTALL_DIR}" ] || (curl -LsSf https://astral.sh/uv/install.sh | sh -s - --quiet)
	$(UVE) python install $(PYV)
	rm -rf .venv
	$(UVE) venv --python=$(PYV) --relocatable --link-mode=copy --seed
	$(UVE) pip install --upgrade pip


RAN := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

runAct:
	echo "source .venv/bin/activate; rm /tmp/$(RAN)" > /tmp/$(RAN)
	bash --init-file /tmp/$(RAN)

runChecks:
	$(UVE) run lefthook run pre-commit --all-files -f

runDocs:
	$(UVE) run zensical build -f $(CONFIG_DOCS)

serveDocs:
	$(UVE) run zensical serve -f $(CONFIG_DOCS) -a 0.0.0.0:8000

runTests:
	$(UVE) run tox

runBuild:
	$(UVE) build

runBump:
	$(UVE) run cz bump --files-only --yes --changelog
	git add .
	$(UVE) run cz version --project | xargs -i git commit -am "bump: release {}"

runLock runUpdate: %: export_%
# add all packages required to be build
	$(UVE) export --package microbial_strain_data_model --frozen --format requirements.txt > packages/microbial_strain_data_model/requirements.txt
	$(UVE) export --package microbial_strain_data_utils --frozen --format requirements.txt > packages/microbial_strain_data_utils/requirements.txt
	$(UVE) export --frozen --only-group dev --format requirements.txt > configs/requirements/dev/requirements.txt
	$(UVE) export --frozen --only-group test --format requirements.txt > configs/requirements/test/requirements.txt
	$(UVE) export --frozen --only-group docs --format requirements.txt > configs/requirements/docs/requirements.txt


export_runLock:
	$(UVE) lock

export_runUpdate:
	$(UVE) lock -U

com commit:
	echo "" > .commit_msg
	@if curl -sf http://ollama:11434; then \
		$(MAKE) message; \
	else\
		$(UVE) run cz commit; \
	fi
	echo "" > .commit_msg

recom recommit:
	@if curl -sf http://ollama:11434; then \
		[ -s .commit_msg ] || (echo "Missing commit message!" && exit 1); \
		git commit -F .commit_msg; \
	else\
		$(UVE) run cz commit --retry; \
	fi
	echo "" > .commit_msg

message:
	git diff --staged -- . ':(exclude)*requirements*.txt' | \
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

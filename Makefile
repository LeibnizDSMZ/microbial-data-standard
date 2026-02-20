ROOT_MAKEFILE:=$(abspath $(patsubst %/, %, $(dir $(abspath $(lastword $(MAKEFILE_LIST))))))

include $(ROOT_MAKEFILE)/.env

export
export PATH := $(PATH):$(shell pwd)/$(UV_INSTALL_DIR)

$(eval UVEL := $(shell which uv && echo "true" || echo ""))
UVE = $(if ${UVEL},'uv',$(UV_INSTALL_DIR)/uv)

dev: setup setupGit
	$(UVE) sync --frozen --all-groups
	$(UVE) run lefthook uninstall 2>&1 || echo "not installed"
	rm -f .git/hooks/*
	$(UVE) run lefthook install

tests: setup
	$(UVE) sync --frozen --group test

build: setup
	$(UVE) sync --frozen

docs: setup
	$(UVE) sync --frozen --group docs

setupGit:
	git config core.editor vim
	git lfs install --force || echo '[FAIL] git-lfs could not be installed'

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
	$(UVE) run mkdocs build -f configs/dev/mkdocs.yml -d ../../public

serveDocs:
	$(UVE) run mkdocs serve -f configs/dev/mkdocs.yml

runTests:
	$(UVE) run tox

runBuild:
	$(UVE) build

runBump:
	$(UVE) run cz bump --files-only --yes --changelog
	git add .
	$(UVE) run cz version --project | xargs -i git commit -am "bump: release {}"

runUV:
	$(UVE) run $(CMD)

runLock runUpdate: %: export_%
# add all packages rquired to be build
	$(UVE) export --frozen --format requirements.txt > requirements.txt
	$(UVE) export --frozen --only-group dev --format requirements.txt > configs/dev/requirements.dev.txt
	$(UVE) export --frozen --only-group test --format requirements.txt > configs/dev/requirements.test.txt
	$(UVE) export --frozen --only-group docs --format requirements.txt > configs/dev/requirements.docs.txt

export_runLock:
	$(UVE) lock

export_runUpdate:
	$(UVE) lock -U

com commit:
	$(UVE) run cz commit

recom recommit:
	$(UVE) run cz commit --retry

buildSchema:
	$(UVE) run bin/python/build_docs_schema_excel.py
	$(UVE) run bin/python/schema_parser_mermaid.py

POETRY = $(HOME)/.local/bin/poetry
PYV = 3.13.2

dev: setup
	$(POETRY) install --with test,docs,dev
	$(POETRY) run lefthook uninstall | echo "lefthook not installed"
	$(POETRY) run lefthook install
	bash bin/deploy/post.sh

tests: setup
	$(POETRY) install --without docs,dev

build: setup
	$(POETRY) install --without test,docs,dev

docs: setup
	$(POETRY) install --with docs --without test,dev

setup:
	git lfs install || echo '[FAIL] git-lfs could not be installed'
	pyenv install $(PYV) -s
	pyenv local $(PYV)
	curl -sSL https://install.python-poetry.org | python3 -
	$(POETRY) env remove --all
	$(POETRY) config virtualenvs.in-project true
	$(POETRY) config virtualenvs.create true
	$(POETRY) env use `pyenv which python`
	$(POETRY) run pip install --upgrade pip

uninstall:
	pyenv local $(PYV)
	curl -sSL https://install.python-poetry.org | python3 - --uninstall

runAct:
	$(POETRY) shell

runChecks:
	$(POETRY) run lefthook run pre-commit --all-files -f

runDocs:
	$(POETRY) run mkdocs build -f configs/dev/mkdocs.yml -d ../../public

serveDocs:
	$(POETRY) run mkdocs serve -f configs/dev/mkdocs.yml

runTests:
	$(POETRY) run tox

runBuild:
	$(POETRY) build

runBump:
	$(POETRY) run cz bump

runPoetry:
	$(POETRY) run $(CMD)

runLock runUpdate: %: export_%
	$(POETRY) export -f requirements.txt -o requirements.txt
	$(POETRY) export --only=dev -f requirements.txt -o configs/dev/requirements.dev.txt
	$(POETRY) export --only=test -f requirements.txt -o configs/dev/requirements.test.txt

export_runLock:
	$(POETRY) lock

export_runUpdate:
	$(POETRY) update --with test,docs,dev

com commit:
	$(POETRY) run cz commit

recom recommit:
	$(POETRY) run cz commit --retry

buildSchema:
	python3 bin/python/build_docs_schema_excel.py
	python3 bin/python/schema_parser_mermaid.py

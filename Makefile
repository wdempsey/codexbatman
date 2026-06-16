.PHONY: docs docs-serve

.venv/bin/mkdocs: requirements.txt
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt

docs: .venv/bin/mkdocs
	./.venv/bin/mkdocs build

docs-serve: .venv/bin/mkdocs
	./.venv/bin/mkdocs serve

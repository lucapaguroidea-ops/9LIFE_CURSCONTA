PY ?= python3

.PHONY: tot build plan module documente intrebari verifica curat

tot: build documente intrebari verifica

build: plan module

plan:
	$(PY) build/build_plan.py

module:
	$(PY) build/build_module.py

documente:
	$(PY) build/documente.py

intrebari:
	$(PY) build/intrebari.py

verifica:
	$(PY) build/verifica.py

curat:
	rm -f dist/*.xlsx dist/*.md dist/*.docx dist/*.html
	find . -name __pycache__ -type d -exec rm -rf {} +

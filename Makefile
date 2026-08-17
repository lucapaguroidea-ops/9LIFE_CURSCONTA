PY ?= python3

.PHONY: tot build plan module verifica curat

tot: build verifica

build: plan module

plan:
	$(PY) build/build_plan.py

module:
	$(PY) build/build_module.py

verifica:
	$(PY) build/verifica.py

curat:
	rm -f dist/*.xlsx
	find . -name __pycache__ -type d -exec rm -rf {} +

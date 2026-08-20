PY ?= python3

.PHONY: tot build plan module documente intrebari parcurs verifica curat

# `parcurs` citește workbook-urile construite (harta de referință e chiar tabelul de
# structură din Legendă), deci vine după `build`.
tot: build documente intrebari parcurs verifica

build: plan module

plan:
	$(PY) build/build_plan.py

module:
	$(PY) build/build_module.py

documente:
	$(PY) build/documente.py

intrebari:
	$(PY) build/intrebari.py

parcurs:
	$(PY) build/parcurs.py

verifica:
	$(PY) build/verifica.py

curat:
	rm -f dist/*.xlsx dist/*.md dist/*.docx dist/*.html
	find . -name __pycache__ -type d -exec rm -rf {} +

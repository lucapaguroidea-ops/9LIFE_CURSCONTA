PY ?= python3

.PHONY: tot build plan module documente intrebari parcurs verifica curat

# `parcurs` citește workbook-urile construite (harta de referință e chiar tabelul de
# structură din Legendă), deci vine după `build`.
tot: build documente intrebari parcurs pachet verifica

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

# `pachet` adună livrabilele de uz; are nevoie de .html-uri, deci după `documente`
pachet:
	$(PY) build/pachet.py

verifica:
	$(PY) build/verifica.py

curat:
	rm -rf dist/pachet dist/pachet-9life.zip
	rm -f dist/*.xlsx dist/*.md dist/*.docx dist/*.html
	find . -name __pycache__ -type d -exec rm -rf {} +

#!/usr/bin/env bash
set -euo pipefail
pip install -r Sitio_SENATI/requirements.txt
python Personal/03_NO_SUPERVISADO_1/01_RETO_PAPELERIA/entrenar.py
python Personal/03_NO_SUPERVISADO_1/02_RETO_LABORATORIO/entrenar.py
python Personal/04_NO_SUPERVISADO_2/RETO_01_BIBLIOTECA/entrenar.py
python Personal/04_NO_SUPERVISADO_2/RETO_02_SENSORES/entrenar.py
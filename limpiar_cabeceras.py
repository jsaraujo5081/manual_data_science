"""
Deja en la cabecera (YAML) de cada capítulo solo title, subtitle y jupyter.
El resto de la configuración (idioma, formato, tabla de contenido, etc.)
vive en _quarto.yml, así un cambio se aplica a todo el libro a la vez.

Uso (desde la carpeta del proyecto):
    python limpiar_cabeceras.py
"""
import re
from pathlib import Path

CLAVES = ("title:", "subtitle:", "jupyter:")

for ruta in sorted(Path(".").glob("c[0-9][0-9]_*.qmd")):
    texto = ruta.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texto, flags=re.S)
    if not m:
        print(f"Sin cabecera YAML, se omite: {ruta}")
        continue
    lineas = [l for l in m.group(1).split("\n") if l.startswith(CLAVES)]
    nuevo = "---\n" + "\n".join(lineas) + "\n---\n" + texto[m.end():]
    if nuevo != texto:
        ruta.write_text(nuevo, encoding="utf-8")
        print(f"Cabecera simplificada: {ruta}")
    else:
        print(f"Ya estaba simplificada: {ruta}")

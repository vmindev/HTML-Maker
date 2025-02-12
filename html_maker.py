import re
import markdown
from pathlib import Path

ruta_texto:Path = Path(__file__).parent/"texto.txt"
ruta_html_nuevo:Path = Path(__file__).parent/"documento.html"
ruta_html_base:Path = Path(__file__).parent/"base.html"

# Almacenamos el contenido del archivo de texto
with open(ruta_texto, "r", encoding="utf-8") as file:
    contenido_texto:str = file.read()
# Convertimos el contenido en HTML
html:str = markdown.markdown(contenido_texto, extensions=["extra"])
html = html.split("\n")
# Conseguimos el html base
with open(ruta_html_base, "r", encoding="utf-8") as file:
    html_base:list = file.readlines()
# Buscamos el indice de </body> en la lista 'html_base'
patron_cierre_body = r"^\s*</body>\s*$" # Patrón de búsqueda para </body>
for i, linea in enumerate(html_base):
    if re.match(patron_cierre_body, linea):
        index:int = i
        break
# Añadimos un salto de pagina al final de cada linea en el html
html = list(map(lambda linea: linea+"\n", html))
# Introducimos el html en la lista 'html_base' dentro de la etiqueta <body>
for linea in html:
    html_base.insert(index, linea)
    index += 1
html = html_base
# Almacenamos el html en un archivo
with open(ruta_html_nuevo, "w", encoding="utf-8") as file:
    list(map(lambda linea: file.write(linea), html))
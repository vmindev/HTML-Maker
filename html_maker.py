import re
import markdown
from pathlib import Path

ruta_texto:Path = Path(__file__).parent/"texto.txt"
ruta_html_nuevo:Path = Path(__file__).parent/"documento.html"
ruta_html_base:Path = Path(__file__).parent/"base.html"

# Almacenamos el contenido del archivo de texto
with open(ruta_texto, "r", encoding="utf-8") as file:
    contenido_texto:str = file.readlines()
# Arreglamos el formato de las listas
patron_lista = r"^(\s*)(-|\d+(?:\.\d+)*\.)\s+(.+)$"
texto:str = ""
temp_text = []
for linea in contenido_texto:
    linea_normal:bool = True
    if match:=re.match(patron_lista, linea): # Esta linea es una lista
        indent, tag, contenido = match.groups()
        indent = len(indent)
        if (indent%3 == 0) and (indent != 0): # La identacion está mal formateada (En espacios de 3)
            linea_normal = False
            indent = (indent//3)*4 # Corregimos el formato de identacion
            espacios = " "*indent
            texto += f"{espacios}{tag} {contenido}\n"
            
    if linea_normal: texto += linea
# Convertimos el contenido en HTML
html:str = markdown.markdown(texto, extensions=["extra"])
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
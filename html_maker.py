import re
import markdown
from pathlib import Path

ruta_texto:Path = Path(__file__).parent/"texto.txt"
ruta_html_nuevo:Path = Path(__file__).parent/"documento.html"
ruta_html_base:Path = Path(__file__).parent/"base.html"

def leer(ruta:Path): # Lee el archivo de la ruta y devuelve el contenido en forma de lista
    datos:list = []
    with open(ruta, "r", encoding="utf-8") as file:
        for linea in file:
            datos.append(linea.strip("\n"))
    return datos

def convert_html(texto_original:list): # Devuelve el texto formateado a html
    texto:list = texto_original.copy()
    
    return texto

def almacenar(ruta:Path, html_base:list, html_texto:list): # Almacena el contenido de 'texto_html' en un archivo html con una plantilla
    # Patrón de búsqueda para </body>
    patron_cierre_body = r"^\s*</body>\s*$"
    # Buscamos el indice de </body> en la lista 'html'
    for i, linea in enumerate(html_base):
        if re.match(patron_cierre_body, linea):
            index:int = i
            break
    # Introducimos el texto con formato html en la lista 'html'
    for linea in html_texto:
        html_base.insert(index, linea)
        index += 1
    # Añadimos un salto de pagina al final de cada linea
    html_base = list(map(lambda linea: linea+"\n", html_base))
    # Escribimos el el archivo el html
    with open(ruta, "w", encoding="utf-8") as file:
        list(map(lambda linea: file.write(linea), html_base))

if __name__=="__main__":
    contenido_txt:list = leer(ruta_texto)
    html_base:list = leer(ruta_html_base)
    html_texto:list = convert_html(contenido_txt)
    almacenar(ruta_html_nuevo, html_base, html_texto)

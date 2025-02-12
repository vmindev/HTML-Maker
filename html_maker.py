import re
from pathlib import Path
from modules.headers import del_header, app_header
from modules.lista import sep_lista, app_lista
from modules.saltos_pagina import del_saltos, app_saltos
from modules.bloque import sep_bloque, app_bloque

ruta_texto:Path = Path(__file__).parent/"texto.txt"
ruta_html_nuevo:Path = Path(__file__).parent/"documento.html"
ruta_html_base:Path = Path(__file__).parent/"base.html"

patrones_interiores:dict = {
    "blockquote":r"\>(.*?)",        # Citado
    "strong":r"\*\*(.*?)\*\*",      # Negrita
    "em":r"\*(.*?)\*",              # Cursiva
    "del":r"\~\~(.*?)\~\~",         # Tachada
    "code":r"\`(.*?)\`",            # Formato de codigo
    "a":r"\[(.*?)\]\((.*?)\)",      # Enlace
    "img":r"\!\[(.*?)\]\((.*?)\)",  # Imagen
}


def leer(ruta:Path): # Lee el archivo de la ruta y devuelve el contenido en forma de lista
    datos:list = []
    with open(ruta, "r", encoding="utf-8") as file:
        for linea in file:
            datos.append(linea.strip("\n"))
    return datos

def convert_html(texto_original:list): # Devuelve el texto formateado a html
    texto:list = texto_original.copy()
    # ========== Separamos el texto en: texto sin el bloque concreto y diccionario/lista con indice y texto formateado ==========
    # Saltos de pagina
    sp_list:list = [int] # [indice1, indice2, ...] (indice=indice donde se encuentra originalmente el salto de página)
    texto, sp_list = del_saltos(texto)
    # Headers
    headers_dict:dict = {int:str} # {indice: linea} (indice=indice original) (linea=linea formateada con html)
    texto, headers_dict = del_header(texto)
    # Listas
    lista_dict:dict = {int:str} # {indice: linea} (indice=indice original) (linea=linea formateada con html)
    texto, lista_dict = sep_lista(texto)
    # Bloques de codigo
    bloque_dict:dict = {int:list} # {indice: []} (indice=indice original) ([]=<pre>,linea, linea2, ...,</pre>, linea=<code>linea</code>)
    texto, bloque_dict = sep_bloque(texto)
    # ========== Combinamos el texto de nuevo ==========
    texto = app_bloque(texto, bloque_dict) # Bloque de código
    texto = app_lista(texto, lista_dict) # Listas
    texto = app_header(texto, headers_dict) # Headers
    texto = app_saltos(texto, sp_list) # Saltos de página
    
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

import re
from pathlib import Path
from modules.lista import comprobar_lista
from modules.saltos_pagina import del_saltos, app_saltos

ruta_texto = Path(__file__).parent/"texto.txt"
ruta_html = Path(__file__).parent/"documento.html"

patrones_exteriores = {
        "pre":r"^`{3}(.*)",    # Bloque de codigo
        "ul":r"^-{1} (.+)",     # Lista desordenada
        "ol":r"\d\. (.+)",      # Lista ordenada
        "h1":r"^#{1} (.+)",     # Header 1
        "h2":r"^#{2} (.+)",     # Header 2
        "h3":r"^#{3} (.+)",     # Header 3
        "h4":r"^#{4} (.+)",     # Header 4
        "h5":r"^#{5} (.+)",     # Header 5
        "h6":r"^#{6} (.+)",     # Header 6
    }

patrones_interiores = {
    "blockquote":r"\>(.*?)",        # Citado
    "strong":r"\*\*(.*?)\*\*",      # Negrita
    "em":r"\*(.*?)\*",              # Cursiva
    "del":r"\~\~(.*?)\~\~",         # Tachada
    "code":r"\`(.*?)\`",            # Formato de codigo
    "a":r"\[(.*?)\]\((.*?)\)",      # Enlace
    "img":r"\!\[(.*?)\]\((.*?)\)",  # Imagen
}


def leer(ruta): # Lee el archivo de la ruta y devuelve el contenido
    with open(ruta, "r", encoding="utf-8") as file:
        datos = file.read()
    return datos.split("\n")

def convert_html(texto): # Devuelve el texto formateado a html
    html = ""
    # ==========
    # Formato de listas
    texto, index_list = del_saltos(texto) # Elimina saltos de pagina
    texto = comprobar_lista(texto)
    texto = app_saltos(texto, index_list) # Devuelve los saltos de pagina en los indices de la lista
    # Formato de bloques
    # Formato de headers
    # Formatos de contenido
    # ==========
    return html

def almacenar(ruta, texto_html): # Almacena el contenido de 'texto_html' en un archivo html con una plantilla
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <link href="styles/style.css" rel="stylesheet" type="text/css" />
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            {texto_html}
        </body>
        </html>
    '''
    with open(ruta, "w", encoding="utf-8") as file:
        file.write(html)

if __name__=="__main__":
    contenido_txt = leer(ruta_texto)
    html = convert_html(contenido_txt)
    almacenar(ruta_html, html)

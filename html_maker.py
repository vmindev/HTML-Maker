import re
from pathlib import Path

ruta_texto = Path(__file__).parent/"texto.txt"
ruta_html = Path(__file__).parent/"documento.html"

patron_lista = [{"h1":r"#{1}"}]

def leer(ruta): # Lee el archivo de la ruta y devuelve el contenido
    with open(ruta, "r", encoding="utf-8") as file:
        datos = file.read()
    return datos

def convert_html(texto): # Devuelve el texto formateado a html
    texto = texto.split("\n")
    html = ""
    for i, linea in enumerate(texto):
        if not linea:
            html += "<br />"
        elif linea.startswith("#"):
            html += "<h1>{}</h1>".format(linea.strip("# "))
        elif linea.startswith("##"):
            html += "<h1>{}</h1>".format(linea.strip("## "))
        elif linea.startswith("###"):
            html += "<h1>{}</h1>".format(linea.strip("### "))
        elif linea.startswith("####"):
            html += "<h1>{}</h1>".format(linea.strip("#### "))
        elif linea.startswith("#####"):
            html += "<h1>{}</h1>".format(linea.strip("##### "))
        elif linea.startswith("######"):
            html += "<h1>{}</h1>".format(linea.strip("###### "))
        elif linea.startswith("```"):
            j = i+1
            while True:
                if texto[j].startswith("```"):
                    break
                else:
                    j += 1
        elif linea:
            print("")
        elif linea:
            print("")
    
    
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

from pathlib import Path

ruta_texto = Path(__file__).parent/"texto.txt"
ruta_html = Path(__file__).parent/"documento.html"

def leer(ruta): # Lee el archivo de la ruta y devuelve el contenido
    with open(ruta, "r", encoding="utf-8") as file:
        datos = file.read()
    return datos

def convert_html(texto): # Devuelve el texto formateado a html
    texto = texto.split("\n")
    html = ""
    for linea in texto:
        if not linea:
            print("Linea vacia")
        elif (1+1):
            pass
    
    
    return html

def almacenar(ruta, texto_html): # Almacena el contenido de 'texto_html' en un archivo html con una plantilla
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
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

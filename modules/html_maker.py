import re
import markdown
from pathlib import Path
from bs4 import BeautifulSoup

def read_lines(ruta_archivo:Path): # Devuelve una lista con el contenido de un archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        contenido:list = file.readlines()
    return contenido

def fix_list_format(texto_original:list): # Devuelve el texto en forma de string con las identaciones formateadas
    patron_lista:str = r"^(\s*)(-|\d+(?:\.\d+)*\.)\s+(.+)$"
    texto:str = ""
    for line in texto_original:
        is_normal_line:bool = True
        if match:=re.match(patron_lista, line): # Esta linea es una lista
            indent, tag, content = match.groups()
            indent = len(indent)
            if (indent%3 == 0) and (indent != 0): # La identacion está mal formateada (En espacios de 3)
                is_normal_line = False
                indent = (indent//3)*4 # Corregimos el formato de identacion
                espacios = " "*indent
                texto += f"{espacios}{tag} {content}\n"
        if is_normal_line: texto += line
    return texto

def index_patron(patron, lista): # Devuelve el indice+1 del patron en la lista
    for i, linea in enumerate(lista):
        if re.match(patron, linea):
            index:int = i+1
            break
    return index

def html_into_html_base(html:list, index:int, base:list): # Devuelve un string con el html resultante
    for linea in html:
        base.insert(index, linea)
        index += 1
    texto = ""
    for linea in base:
        texto += linea
    return texto

def obtener_titulo(text:list):
    title:str
    for line in text:
        if line != "\n" and line:
            title = line.strip("\n").strip("#")
            break
    return title

def main(ruta_texto:Path, ruta_html_base:Path, dir_ruta_html_nuevo:Path):
    # Almacenamos el contenido de los archivos
    texto_list:list = read_lines(ruta_texto)
    titulo = obtener_titulo(texto_list)
    html_base:list = read_lines(ruta_html_base)
    # Arreglamos el formato de las listas
    texto:str = fix_list_format(texto_list)
    # Formateamos el texto a HTML
    html_list:list = (markdown.markdown(texto, extensions=["extra"])).split("\n")
    # Buscamos el indice de <div class="content"> en la lista 'html_base'
    patron_html = r"^\s*<div class=\"content\">\s*$" # Patrón de búsqueda para <div class="content">
    index:int = index_patron(patron_html, html_base)
    # Añadimos un salto de pagina al final de cada linea en la lista html
    html_list = list(map(lambda linea: linea+"\n", html_list))
    # Introducimos el html de 'html_list' en la lista 'html_base' dentro de la etiqueta <div class="content">
    html:str = html_into_html_base(html_list, index, html_base)
    # Corregimos las identaciones del HTML
    soup = BeautifulSoup(html, "html.parser")
    html:str = soup.prettify()
    # Almacenamos el html en un archivo
    with open(dir_ruta_html_nuevo/f"{titulo}.html", "w", encoding="utf-8") as file:
        file.write(html)

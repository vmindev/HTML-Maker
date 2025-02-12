import re

patron = r"^(#+)\s+(.+)$"

def del_header(texto:list): # Devuelve el texto sin headers y un diccionario {indice:linea}
    texto_no_header:list = []
    header_dict:dict = {} # Diccionario de la forma: {indice:<hx>contenido</hx>} hx=(h1,h2,...)
    for i, linea in enumerate(texto):
        if match:=re.match(patron, linea):
            header, content = match.groups()
            header = "h{}".format(len(header))
            header_dict.update({i:"<{}>{}</{}>".format(header, content, header)})
        else:
            texto_no_header.append(linea)
    return texto_no_header, header_dict

def app_header(texto:list, diccionario:dict): # Devuelve el texto combinado
    texto:list = texto.copy()
    for indice, linea in diccionario.items():
        texto.insert(indice, linea)
    return texto

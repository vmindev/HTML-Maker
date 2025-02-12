import re

patrones = {
    "ul":r"^( *)(-) (.+)",     # Lista desordenada
    "ol":r"^( *)(\d+\.) (.+)"     # Lista ordenada
}

def sep_lista(texto:list): # Devuelve el texto original sin listas y un diccionario {index:[linea_content, indent_level, tag]}
    texto_no_list = []
    texto_dict = {}
    for i, linea in enumerate(texto):
        if match:=re.match(patrones["ul"], linea): # Linea tiene formato de lista desordenada
            tag = "ul"
            indent, _, content = match.groups()
            content = "<li>{}</li>".format(content)
            texto_dict.update({i:[content, len(indent)//3, tag]})
        elif match:=re.match(patrones["ol"], linea): # Linea tiene formato de lista ordenada
            tag = "ol"
            indent, _, content = match.groups()
            content = "<li>{}</li>".format(content)
            texto_dict.update({i:[content, len(indent), tag]})
        else:
            texto_no_list.append(linea)
    return texto_no_list, format_lista(texto_dict)
    

def format_lista(diccionario:dict): # Devuelve el diccionario con el texto formateado
    # Creamos dos listas con el contenido del diccionario que necesitamos
    array = list(map(lambda x: [x[0],x[1],x[2]], list(diccionario.values())))
    indices_lista = list(map(lambda x: x, list(diccionario.keys())))
    # Formateamos las lineas
    diccionario_nuevo = {}
    buffer = []
    for i,lista in enumerate(array):
        '''Asignamos valores necesarios'''
        linea = lista[0]
        act_lvl = lista[1]
        tag = lista[2]
        # Calculamos el nivel de identación previo
        if i == 0: # Primera línea
            prev_lvl = -1
        else:
            prev_lvl = array[i-1][1]
        # Calculamos el nivel de identación próximo
        if i == (len(array)-1): # Última línea
            prox_lvl = -1
        else:
            prox_lvl = array[i+1][1]
        '''Verificamos si hay que abrir una nueva lista'''
        if act_lvl > prev_lvl: # Hay que abrir lista
            linea = f"<{tag}>{linea}" # Añadimos el tag a la izquierda para abrir lista
            buffer.append(tag) # Añadimos el tag al buffer
        '''Verificamos si hay que cerrar una lista'''
        if act_lvl > prox_lvl: # Hay que cerrar lista
            for _ in range(act_lvl-prox_lvl): # Se repite tantas veces como tags haya que cerrar
                linea += "</{}>".format(buffer.pop()) # Añadimos el tag al final

        diccionario_nuevo.update({indices_lista[i]: linea})
    return diccionario_nuevo

def app_lista(texto:list, diccionario:dict):
    texto:list = texto.copy()
    diccionario:dict = diccionario.copy()
    for index, linea in diccionario.items():
        texto.insert(index, linea)
    return texto

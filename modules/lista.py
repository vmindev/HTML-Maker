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


def asign_values(lista:list, array:list, i:int): # Procesa los datos y los devuelve en forma de variables
    linea:str = lista[0] # Texto
    act_tag:str = lista[2] # Etiqueta html
    act_lvl:int = lista[1] # Nivel de identación actual
    # Calculamos el nivel de identación previo
    if i == 0: prev_lvl: int = -1 # Primera línea
    else: prev_lvl: int = array[i-1][1] # Linea normal
    # Calculamos el nivel de identación próximo
    if i == (len(array)-1): prox_lvl: int = -1 # Ultima línea
    else: prox_lvl: int = array[i+1][1] # Linea normal
    # Calculamos el tag anterior
    if i == 0: prev_tag:str = None
    else: prev_tag:str = array[i-1][2]
    
    return linea, act_tag, prev_tag, act_lvl, prev_lvl, prox_lvl

def calculate_open_close_list(actual:int, previo:int, proximo:int, tag:str, buffer:list): # Devuelve dos booleanos para indicar apertura/cierre de lista y el numero de listas a cerrar
    num_cierre: int=0
    # Valores predefinidos de apertura y cierre
    open:bool = False
    close:bool = False
    # Calculamos si hay que abrir una nueva lista
    if actual > previo:
        open = True
    if tag != buffer[len(buffer-1)]:
        open = True
    # Calculamos si hay que cerrar una lista
    if actual > proximo:
        close = True
        num_cierre = (actual-proximo) # Numero de listas que hay que cerrar
    
    return open, close, num_cierre

def open_close_list(linea:str, open:bool, close:bool, tag:str, buffer:list, num_cierre:int, indent:int): # Devuelve la linea formateada y el buffer
    buffer = buffer.copy()
    if open:
        linea = f"<{tag}>{linea}" # Añadimos el tag a la izquierda para abrir lista
        buffer.append({tag: indent}) # Añadimos al buffer el tag y el nivel de identacion
    if close:
        for _ in range(num_cierre): # Se repite tantas veces como tags haya que cerrar
            linea += "</{}>".format(x for x in (buffer.pop()).keys()) # Añadimos el tag al final
    
    return linea, buffer

def format_lista(diccionario:dict): # Devuelve el diccionario con el texto formateado
    # Creamos dos listas con el contenido del diccionario que necesitamos
    array = list(map(lambda x: [x[0],x[1],x[2]], list(diccionario.values())))
    indices_lista = list(map(lambda x: x, list(diccionario.keys())))
    # Formateamos las lineas
    diccionario_nuevo:dict = {}
    buffer:list = [] # [{tag:indent},{...},...]
    for i,lista in enumerate(array):
        '''Asignamos valores necesarios'''
        linea, act_tag, prev_tag, act_lvl, prev_lvl, prox_lvl = asign_values(lista, array, i)
        '''Calculamos apertura/cierre de listas'''
        abrir_lista, cerrar_lista, num_cierre = calculate_open_close_list(act_lvl, prev_lvl, prox_lvl, act_tag, buffer)
        '''Abrimos/Cerramos lista'''
        linea, buffer = open_close_list(linea, abrir_lista, cerrar_lista, act_tag, buffer, num_cierre, act_lvl)
        # Guardamos el contenido de la linea en el diccionario nuevo
        diccionario_nuevo.update({indices_lista[i]: linea})
    
    return diccionario_nuevo

def app_lista(texto:list, diccionario:dict):
    texto:list = texto.copy()
    diccionario:dict = diccionario.copy()
    for index, linea in diccionario.items():
        texto.insert(index, linea)
    return texto

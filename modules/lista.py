import re

patrones = {
    "ul":r"^( *)(-) (.+)",     # Lista desordenada
    "ol":r"^( *)(\d+\.) (.+)"     # Lista ordenada
}

def sep_lista(texto): # Devuelve el texto original sin listas y un diccionario {index:[linea_content, indent_level, tag]}
    texto_no_list = []
    texto_dict = {}
    for i, linea in enumerate(texto):
        if match:=re.match(patrones["ul"], linea): # Linea tiene formato de lista desordenada
            tag = "ul"
            indent, _, content = match.groups()
            texto_dict.update({i:[content, len(indent)//3, tag]})
        elif match:=re.match(patrones["ol"], linea): # Linea tiene formato de lista ordenada
            tag = "ul"
            indent, _, content = match.groups()
            texto_dict.update({i:[content, len(indent), tag]})
        else:
            texto_no_list.append(linea)
    
    return texto_no_list, texto_dict

def formato_lista(lista_dict):
    for lista in lista_dict.values():
        
        pass

def app_lista(texto):
    texto = texto.copy()
    tags = []
    level = -1
    level_anterior = -1
    for i, linea in enumerate(texto):
        #===== Comprobamos el valor de la linea =====
        # Comprobamos si no es una lista
        if not (re.match(patrones["ul"],linea) or re.match(patrones["ol"],linea)):
            level = -1
        else: # Es una lista
            # Lista desordenada
            if match:= re.match(patrones["ul"],linea):
                tag = "ul"
                indent, _, content = match.groups()
                level_anterior = level
                level = len(indent) // 2 # Nivel de identación de la línea
            # Lista ordenada
            elif match:= re.match(patrones["ol"],linea):
                tag = "ol"
                indent, _, content = match.groups()
                level_anterior = level
                level = len(indent) // 2 # Nivel de identación de la línea
        
        '''Verificamos lo que se debe hacer a la lista'''
        if level == -1: # No es lista
            # Comprobamos si la linea anterior es una lista
            if level_anterior != -1: # Si es una lista, cerramos la lista anterior
                for _ in range(level_anterior-level):
                    texto[i-1] += f"</{tags.pop()}>" 
            else: # No es una lista
                pass
        
        elif level > level_anterior: # Lista nueva
            # Añadimos la apertura de lista
            texto[i] = f"<{tag}>"+f"<li>{content}</li>"
            # Añadimos el tag de apertura a la lista de tags
            tags.append(tag)
        
        elif level == level_anterior: # Sigue la lista
            texto[i] = f"<li>{content}</li>"
        elif level < level_anterior: # Cerramos la lista anterior
            for _ in range(level_anterior-level):
                texto[i-1] += f"</{tags.pop()}>"
            texto[i] = f"<li>{content}</li>"
        
    return texto
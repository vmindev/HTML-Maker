import re

patron = r"^`{3}(.*)"

def sep_bloque(texto): # Devuelve el texto original sin bloques y un diccionario {indice_original:[bloque]}
    texto_no_bloque = []
    dict_bloque = {}
    in_bloque = False
    
    for i,linea in enumerate(texto):
        if re.match(patron, linea): # Linea con formato de bloque
            # Cambiamos el valor de la "variable bandera"
            if in_bloque:
                in_bloque = False # Cierre de bloque
                dict_bloque[indice].append("</pre>")
            else:
                in_bloque = True # Apertura de bloque
                indice = i
                dict_bloque.update({indice:[]})
                dict_bloque[indice].append("<pre>") # etiqueta de apertura
        else: # Linea sin formato de bloque
            if in_bloque: # Dentro de bloque
                dict_bloque[indice].append(f"<code>{linea}</code>")
            else: # Fuera de bloque
                texto_no_bloque.append(linea)
    return texto_no_bloque, dict_bloque 

def app_bloque(texto, dict_bloque): # Devuelve el texto unido
    texto = texto.copy()
    for indice, bloque in dict_bloque.items():
        for linea in bloque:
            texto.insert(indice, linea)
            indice += 1
    return texto

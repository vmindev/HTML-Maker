def del_saltos(texto:list): # Devuelve el texto sin saltos de linea y una lista con los indices.
    texto = texto.copy()
    texto_no_sp:list = []
    index_list:list = []
    for index, linea in enumerate(texto):
        if linea: # No es un salto de pagina
            texto_no_sp.append(linea)
        else: # Es un salto de pagina
            index_list.append(index)
    return texto_no_sp, index_list

def app_saltos(texto:list, index_list:list): # Devuelve el texto proporcionado con los saltos de linea añadidos en cada indice de 'index_list'
    texto = texto.copy()
    for index in index_list:
        texto.insert(index, "<br />")
    return texto

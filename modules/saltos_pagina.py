texto = [
    "Texto 1",
    "Texto 2",
    "",
    "Texto 3",
    "Texto 4",
    "",
    "Texto 5",
    "",
    "Texto 6"
]

def del_saltos(texto_lista): # Devuelve el texto sin saltos de linea y una lista con los indices.
    texto = texto_lista.copy()
    saltos_indices = []
    for i in range(texto.count("")):
        saltos_indices.append(texto.index(""))
        texto.pop(saltos_indices[i])
    return texto, saltos_indices

def app_saltos(texto_lista, index_list): # Devuelve el texto proporcionado con los saltos de linea añadidos en cada indice de 'index_list'
    texto = texto_lista.copy()
    for index in reversed(index_list):
        texto.insert(index, "")
    return texto

texto, indices = del_saltos(texto)
texto = app_saltos(texto, indices)

diccionario = {
    1: "hola",
    2: "buenas",
    3: "tardes",
    4: "encantado"
}

def transformar(dicc:dict, i:int=0): # Comentario
    dicc = dicc.copy()
    for clave in dicc.keys():
        dicc[clave] = i
        i += 1
    return dicc


list(map(lambda x: print(x), diccionario.values()))

# Cambiamos los valores del diccionario
nuevo_diccionario = transformar(dicc=diccionario)
print()
list(map(lambda x: print(x), diccionario.values()))
print()
list(map(lambda x: print(x), nuevo_diccionario.values()))


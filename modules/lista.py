import re

texto = [   
            "Texto normal",
            "- Item 1",
            "  - Item 1.1",
            "    - Item 1.1.1",
            "    - Item 1.1.2",
            "      1. Item 1.1.2.1",
            "        - Item 1.1.2.1.1",
            "  - Item 1.2",
            "  - Item 1.3",
            "- Item 2",
            "  1. Item 2.1",
            "  2. Item 2.2",
            "Texto normal"
        ]

patrones = {
    "ul":r"^( *)(-) (.+)",     # Lista desordenada
    "ol":r"^( *)(\d+\.) (.+)"     # Lista ordenada
}

def compr_lista(texto_original):
    texto = texto_original.copy()
    tags = []
    level_anterior = -1
    for i, linea in enumerate(texto):
        # Comprobamos si la linea es una lista
        for nombre, patron in patrones.items():
            if match:= re.match(patron, linea):
                indent, _, content = match.groups()
                level_anterior = level
                level = len(indent) // 2 # Nivel de identación de la línea
                break
            else: # La linea no es una lista
                level = -1
        
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
            texto[i] = f"<{nombre}>"+f"<li>{content}</li>"
            # Añadimos el tag de apertura a la lista de tags
            tags.append(nombre)
        
        elif level == level_anterior: # Sigue la lista
            texto[i] = f"<li>{content}</li>"
        
        elif level < level_anterior: # Cerramos la lista anterior
            for _ in range(level_anterior-level):
                texto[i-1] += f"</{tags.pop()}>"
            texto[i] = f"<li>{content}</li>"
        
    return texto
        

texto_formato_listas = compr_lista(texto_original=texto)
for linea in texto_formato_listas:
    print(linea)
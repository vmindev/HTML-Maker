from pathlib import Path
import re


ruta = Path("texto de pruebas.txt")

with open(ruta, "r", encoding="utf-8") as file:
    texto = file.read()
    texto = texto.split("\n")

patrones_exteriores = {
        "pre":r"^`{3}(.*)",    # Bloque de codigo
        "ul":r"^-{1} (.+)",     # Lista desordenada
        "ol":r"\d\. (.+)",      # Lista ordenada
        "h1":r"^#{1} (.+)",     # Header 1
        "h2":r"^#{2} (.+)",     # Header 2
        "h3":r"^#{3} (.+)",     # Header 3
        "h4":r"^#{4} (.+)",     # Header 4
        "h5":r"^#{5} (.+)",     # Header 5
        "h6":r"^#{6} (.+)",     # Header 6
    }

patrones_interiores = {
    "strong":r"\*\*(.+)\*\*",   # Negrita
    "em":r"\*(.+)\*",           # Cursiva
    "del":r"\~\~(.+)\~\~",      # Tachada
    "code":r"\`(.+)\`",         # Formato de codigo
    "blockquote":r"\>(.+)",     # Citado
    "a":r"\[(.+)\]\((.+)\)",    # Enlace
    "img":r"\!\[(.+)\]\((.+)\)" # Imagen
}

def busqueda_patron_in(cadena, patrones): # Busca si hay un patron interior en la cadena proporcionada
    
    pass

def busqueda_patron_ex(texto, patrones_ex, patrones_in): # Busca si hay un patron exterior en el texto proporcionado
    i = 0
    while i < len(texto): # 'i' indica el numero de fila que se está consultando
        print("===============================================================================")
        print(f"Busqueda en la linea: [{texto[i]}]")
        for nombre, patron in patrones_ex.items():
            if resultado := re.search(patron, texto[i]): # Si se encuentra un resultado que coincida con el 'patron'
                if nombre == "pre": # Si el 'patron' es un bloque de codigo
                    print(f"---->\nPatron encontrado:[{nombre}] ~ Contenido:[{resultado.group(1)}]")
                    contenido_pre = [] # Lista con el contenido del bloque
                    i += 1 # Saltamos a la linea siguiente
                    while (resultado := re.search(patrones_ex["pre"], texto[i])) == None:
                        contenido_pre.append(texto[i]) # Añadimos a la lista de contenido la linea actual
                        i += 1 # Saltamos a la linea siguiente
                    # Leemos el contenido del bloque
                    busqueda_patron_ex(contenido_pre, patrones_ex, patrones_in)
                    # Imprimimos el segundo match
                    resultado = re.search(patrones_ex["pre"], texto[i])
                    print(f"---->\nPatron encontrado:[pre] ~ Contenido:[{resultado.group(1)}]")
                else:
                    print(f"Patron encontrado:[{nombre}] ~ Contenido:[{resultado.group(1)}]")
                    print("Contenido HTML:[<{}>{}<{}>]".format(nombre, resultado.group(1), nombre))
        print("===============================================================================\n")
        i += 1


if __name__=="__main__":
    patron = patrones_exteriores["pre"]
    busqueda_patron_ex(texto, patrones_exteriores, patrones_interiores)

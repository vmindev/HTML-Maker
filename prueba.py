import re

texto = "Texto de **una** cadena *de prueba* **otro strong**"

patron_dobles = r"\*\*(.*?)\*\*"  # Captura contenido entre **dobles asteriscos**
patron_simples = r"\*(?!\*)(.*?)\*"  # Captura contenido entre *simples* (evita **dobles**)

# Buscamos primero el contenido doble
dobles = re.findall(patron_dobles, texto)

# Renombramos **contenido** por <strong>contenido</strong>
texto = re.sub(patron_dobles, r"<strong>\1</strong>", texto)
print(texto)
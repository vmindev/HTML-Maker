import re

texto = "Texto de **una** cadena *de prueba* **otro strong**"
etiqueta = "b"  # Puedes cambiarlo por cualquier etiqueta como "em", "span", etc.

# Patrón para detectar texto entre **dobles asteriscos**
patron_dobles = r"\*\*(.*?)\*\*"

# Reemplazo dinámico usando la variable etiqueta
resultado = re.sub(patron_dobles, rf"<{etiqueta}>\1</{etiqueta}>", texto)

print(resultado)

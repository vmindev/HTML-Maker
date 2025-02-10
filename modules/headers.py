import re
'''
"ul":r"^( *)(-) (.+)",
indent, _, content = match.groups()
'''

texto = [
    "",
    "# Header 1",
    "## Header 2",
    "### Header 3",
    "#### Header 4",
    "##### Header 5",
    "###### Header 6",
    "",
    "Texto normal",
    "1. ## Header 2",
    "Texto normal",
    "",
    "",
    "Texto normal",
    "  - ## Header 2",
    ""
]



def header_format(texto): # Devuelve el texto con formato de headers
    patron = r"^(.*?)(#+)\s+(.+)$"
    texto = texto.copy()
    # ================================================================================
    for i, linea in enumerate(texto):
        match = re.match(patron, linea)
        if match:
            contenido_previo, numero_header, contenido_posterior = match.groups()
            numero_header = len(numero_header)
            texto[i] = contenido_previo
    # ================================================================================
    return texto


texto = header_format(texto)
for linea in texto: print(linea)

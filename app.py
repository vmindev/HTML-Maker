from pathlib import Path
from modules.html_maker import main as main_html_maker

if __name__=="__main__":
    texto_root:Path = Path(__file__).parent/"Respuesta IA/respuesta_IA.txt" # Ruta documento de texto que almacenará la respuesta de la ia
    html_base_root:Path = Path(__file__).parent/"templates/base.html" # Ruta plantilla html base
    html_nuevo_root:Path = Path(__file__).parent/"Respuesta IA/documentacion.html" # Ruta para el archivo html que contiene la pagina creada
    
    # Creamos el html a partir del contenido del archivo de texto
    main_html_maker(texto_root, html_base_root, html_nuevo_root)

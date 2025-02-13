from pathlib import Path
from modules.html_maker import main as main_html_maker
from modules.clone_file import clone_file

if __name__=="__main__":
    carpeta_almacenamiento:Path = Path("C:/Users/alvar/Programacion/python-repo/Bases de datos/htmls") # Ruta de almacenamiento del html resultante (A parte de dentro de Respuesta IA)
    style_root:Path = Path(__file__).parent/"Respuesta IA/styles/style.css" # Ruta archivo de estilo css
    style_root_almacenamiento:Path = Path(carpeta_almacenamiento/"styles/style.css") # Ruta de archivo de estilo css dentro de 'carpeta de almacenamiento'
    texto_root:Path = Path(__file__).parent/"Respuesta IA/respuesta_IA.txt" # Ruta documento de texto que almacenará la respuesta de la ia
    html_base_root:Path = Path(__file__).parent/"templates/base.html" # Ruta plantilla html base
    html_nuevo_root:Path = Path(__file__).parent/"Respuesta IA/documentacion.html" # Ruta para el archivo html que contiene la pagina creada
    # Creamos el html a partir del contenido del archivo de texto
    titulo = main_html_maker(texto_root, html_base_root, html_nuevo_root) # Obtenemos el titulo para archivo
    # Clonamos el archivo html y css en la carpeta de almacenamiento
    try:
        clone_file(html_nuevo_root, carpeta_almacenamiento/f"{titulo}.html")
        # Eliminamos si es posible el anterior archivo de css
        style_root_almacenamiento.unlink()
        clone_file(style_root, style_root_almacenamiento)
    except Exception as e:
        print(f"Error: {e}")
    
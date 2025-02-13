import shutil
from pathlib import Path

def clone_file(origen:Path, destino:Path): # Clona el archivo html en la ruta proporcionada
    '''
    Copia un archivo de la ruta de origen a la ruta de destino.

    Args:
        origen: La ruta al archivo de origen.
        destino: La ruta al archivo de destino.
    '''
    # Si la carpeta no existe la crea
    destino.parent.mkdir(parents=True, exist_ok=True)
    # Copia el archivo
    shutil.copy2(origen, destino)
        
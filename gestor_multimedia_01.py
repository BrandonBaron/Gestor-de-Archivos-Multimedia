"""Este módulo se encarga de gestionar operaciones multimedia."""
import os
import shutil

# Define la ruta base de la carpeta de destino
BASE_PATH = r'D:\Descargas Manager'
DOWNLOAD_FOLDER = BASE_PATH  # O cualquier otra ruta específica que desees utilizar
# Ruta para la carpeta 'Others'(Aqui se guardaran los archivos que no se encuentren en la lista)
OTHERS_FOLDER = os.path.join(BASE_PATH, 'Others')
# Asegúrate de que la carpeta 'Others' existe
if not os.path.exists(OTHERS_FOLDER):
    os.makedirs(OTHERS_FOLDER)
# Puedes agregar otro tipo de archivos
destinations = {
    '.mp3': os.path.join(BASE_PATH, 'Music'),
    '.mp4': os.path.join(BASE_PATH, 'Videos'),
    '.jpg': os.path.join(BASE_PATH, 'Pictures'),
    '.jpeg': os.path.join(BASE_PATH, 'Pictures'),
    '.png': os.path.join(BASE_PATH, 'Pictures'),
    '.gif': os.path.join(BASE_PATH, 'Gifs'),
    '.rar': os.path.join(BASE_PATH, 'Rar'),
    '.zip': os.path.join(BASE_PATH, 'Rar'),
    '.docx': os.path.join(BASE_PATH, 'Word'),
    '.doc': os.path.join(BASE_PATH, 'Word'),
    '.pdf': os.path.join(BASE_PATH, 'PDF'),
    '.pptx': os.path.join(BASE_PATH, 'PowerPoint'),
    '.exe': os.path.join(BASE_PATH, 'Executables'),
    '.msi': os.path.join(BASE_PATH, 'Executables'),
    '.csv': os.path.join(BASE_PATH, 'CSV'),
    '.xlsx': os.path.join(BASE_PATH, 'Excel'),
}

# Crea las carpetas de destino si no existen
for folder in destinations.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Mueve los archivos a las carpetas de destino correspondientes
for filename in os.listdir(DOWNLOAD_FOLDER):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    if os.path.isfile(file_path):  # Se asegura de que sea un archivo
        name, extension = os.path.splitext(filename)
        if extension in destinations:
            destination = destinations[extension]
        else:
            destination = OTHERS_FOLDER  # Usa la carpeta 'Others' para extensiones no listadas

        destination_file_path = os.path.join(destination, filename)

        # Si el archivo ya existe en la carpeta de destino, no lo mueve
        if not os.path.exists(destination_file_path):
            shutil.move(file_path, destination)
        else:
            print(f"El archivo {filename} ya existe en {destination}, no se ha movido.")

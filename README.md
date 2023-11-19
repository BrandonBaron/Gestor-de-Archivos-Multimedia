# Gestor de Archivos Multimedia

Este módulo se encarga de gestionar operaciones multimedia organizando automáticamente los archivos descargados en carpetas específicas basadas en su extensión. Es útil para mantener organizada la carpeta de descargas sin la necesidad de hacerlo manualmente.

## Características

- Organiza archivos multimedia en carpetas específicas por tipo de archivo.
- Soporta una amplia gama de extensiones de archivos como `.mp3`, `.mp4`, `.jpg`, `.docx`, etc.
- Mueve archivos desconocidos o no especificados a una carpeta 'Others'.
- Evita la sobreescritura de archivos existentes.

## Requisitos Previos

Para usar este script, necesitarás:
- Python instalado en tu sistema.
- Acceso a la ruta de la carpeta que deseas organizar.

## Uso

Para usar el script, sigue estos pasos:

1. Asegúrate de que Python esté instalado en tu sistema.
2. Modifica la variable `BASE_PATH` en el script para que apunte a la carpeta que deseas organizar.
3. Ejecuta el script con Python desde la línea de comandos:


python gestor_multimedia.py



El script automáticamente creará las carpetas necesarias si no existen y moverá los archivos a sus respectivas carpetas.

## Personalización

Puedes añadir o eliminar extensiones de archivo y sus carpetas de destino correspondientes en el diccionario `destinations` dentro del script.

## Contribuir

Las contribuciones son bienvenidas. Si tienes una sugerencia para mejorar este gestor, por favor abre un issue o envía un pull request con tus cambios.


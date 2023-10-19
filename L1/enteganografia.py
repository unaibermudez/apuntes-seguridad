import hashlib
import os

# Directorio que contiene las imágenes
directorio_imagenes = 'imagen/'

# Hash que deseas verificar
hash_objetivo = 'e5ed313192776744b9b93b1320b5e268'

# Función para calcular el hash MD5 de una imagen
def calcular_hash_md5(imagen_path):
    hasher = hashlib.md5()
    with open(imagen_path, 'rb') as archivo:
        while True:
            chunk = archivo.read(1024)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

# Recorrer todas las imágenes en el directorio
for imagen_nombre in os.listdir(directorio_imagenes):
    imagen_path = os.path.join(directorio_imagenes, imagen_nombre)
    if os.path.isfile(imagen_path):
        imagen_hash_md5 = calcular_hash_md5(imagen_path)
        if imagen_hash_md5 == hash_objetivo:
            print(f'La imagen que coincide con el hash MD5 es: {imagen_nombre}')

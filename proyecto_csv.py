import csv
import random

# Datos de ejemplo
marca = "marca"
modelos = ["mod1", "mod2", "mod3", "mod4", "mod5"]

preciod = 100
preciop = 10000

linkyt= "link.link.link.link.link"

# Nombre del archivo CSV
nombre_archivo = "datos_autos.csv"

# Crear y escribir en el archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    # Escribir encabezados
    writer.writerow(["Marca", "Modelo", "Preciod","Preciop", "linkyt"])
    
    # Escribir datos aleatorios
    writer.writerow([marca,modelos])

print("Archivo CSV creado exitosamente.")

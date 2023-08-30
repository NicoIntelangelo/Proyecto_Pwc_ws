import csv

# Datos de ejemplo
datos = [
    ["Toyota", ["Corolla", "Camry", "Rav4"]],
    ["Honda", ["Civic", "Accord"]],
    ["Ford", ["Mustang", "F-150"]]
]

# Crear y escribir en el archivo CSV
with open("ejemplo_multiple_celdas.csv", mode='w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    # Escribir encabezados
    writer.writerow(["Marca", "Modelo"])
    
    # Escribir datos
    for marca, modelos in datos:
        # Unir los modelos en una cadena separada por comas
        modelos_str = ", ".join(modelos)
        writer.writerow([marca, modelos_str])

print("Archivo CSV creado exitosamente.")
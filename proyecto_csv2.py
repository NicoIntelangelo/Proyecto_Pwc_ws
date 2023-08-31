import csv

marca= "ford"
modelo = "mustang"
versiones=["v1", "v2", "v3"]
precios_pesos=[100,200,300]
precio_promedio_meli=100
link="link youtube"
cambio_dolar = 10


# Crear y escribir en el archivo CSV
with open("ejemplo_multiple_celdas.csv", mode='w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    
    writer.writerow(["Marca", marca])
    writer.writerow(["Marca", modelo])
    
    versiones_line = ["versiones",]
    for i in range(0,len(versiones)):
        versiones_line.append(versiones[i])
    writer.writerow(versiones_line)
    
    pesos_line = ["pesos",]
    for i in range(0,len(precios_pesos)):
        pesos_line.append(precios_pesos[i])
    writer.writerow(pesos_line)

    dolares_line = ["dolares",]
    for i in range(0,len(precios_pesos)):
        dolares_line.append(int(precios_pesos[i]/cambio_dolar))
    writer.writerow(dolares_line)
    
    writer.writerow(["precio promedio meli", precio_promedio_meli, precio_promedio_meli/cambio_dolar])

    writer.writerow(["link youtube", link])


print("Archivo CSV creado exitosamente.")


import time
import helium as he
import csv


brand = str(input("seleccione la marca: ")).lower()
model = str(input("seleccione el modelo: ")).lower()


#BUSCAR AUTO EN MERCADO LIBRE Y CALCULAR SU PRECIO PROMEDIO

he.start_chrome(f"https://autos.mercadolibre.com.ar/{brand}/{model}/0-km/2023/")

time.sleep(5)


try:
    error_404_meli = he.find_all(he.S("//html/body/main/div/div/div[2]/h3")) 

    if len(error_404_meli) > 0:
        print("Error en la busqueda, intentar nuevamente")
        he.kill_browser()
except Exception as e:
    e = e 


prices = he.find_all(he.S(".andes-money-amount__fraction"))

total = 0

for i in range(0,30):
    clear_num = int(prices[i].web_element.text.replace(".", ""))
    total = total + clear_num

avg_price_meli = int(total/30)


## COTIZACION DOLAR BLUE VENTA
he.go_to("https://dolarhoy.com/cotizaciondolarblue")

dolar_blue = he.find_all(he.S("//html/body/div[3]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]"))


if len(dolar_blue ) > 0 :
    for dolar_blue_value in dolar_blue :
        dolar_blue_value = dolar_blue_value.web_element.text.split(".")[0]
        dolar_blue_value = int(dolar_blue_value.split("$")[1])

avg_price_meli_dolar = int(avg_price_meli/dolar_blue_value)


print("$",avg_price_meli)
print("u$d",int(avg_price_meli/dolar_blue_value))



# BUSCAR EN AUTOCOSMOS
if len(model) >= 1:
    model_ac = model.replace(" ", "-")

he.go_to(f"https://www.autocosmos.com.ar/catalogo/vigente/{brand}/{model_ac}")

time.sleep(3)

error_404_ac = False
try:
    error_404 = he.find_all(he.S(".error-container"))

    if len(error_404) > 0:
        error_404_ac = True
except Exception as e:
    e = e 

if error_404_ac == False:
    #BUSCAR VERSIONES 

    versions = he.find_all(he.S("body section div div table tbody tr td a"))

    all_versions = []

    for i in range(0,len(versions),2):
        all_versions.append(versions[i].web_element.text)
        print(versions[i].web_element.text)
        
    print(all_versions)

    #BUSCAR PRECIOS

    prices = he.find_all(he.S("body section div div table tbody tr td"))

    prices_value = []

    for i in range(1,len(prices),4):
        prices_value.append(prices[i].web_element.text)
        print(prices[i].web_element.text)

    prices_value_converted = []


    if len(prices ) > 0 :
        for price_value in prices_value :
            price_value = price_value.replace(".","")
            price_value = int(price_value.split("$")[1])
            prices_value_converted.append(price_value)

    print(prices_value_converted)

    ## CONVERTIR A DOLARES

    prices_value_converted_dolars = []

    if len(prices ) > 0 :
        for price_value in prices_value_converted :
            prices_value_converted_dolars.append(int(price_value/dolar_blue_value))

    print(prices_value_converted_dolars)



## BUSCAR TEST EN YOUTUBE
he.go_to("https://www.youtube.com/@MatiasAnticoTV/videos")

time.sleep(5)
he.scroll_down(10000)
time.sleep(2)
he.scroll_down(10000)
time.sleep(2)
he.scroll_down(10000)
time.sleep(2)
he.scroll_down(10000)
time.sleep(2)
he.scroll_down(10000)
time.sleep(2)
he.scroll_down(10000)
time.sleep(2)

video_titles = he.find_all(he.S("#video-title"))

video_find = False

if brand == "volkswagen":
    brand_1 = "vw"
else:
    brand_1 = brand

for titles in video_titles:
    if brand_1.lower() and model.lower() in titles.web_element.text.lower():
        he.click(titles)
        video_find = True
        break


if video_find:
    video_url = he.get_driver().current_url
    print(video_url)
else:
    print("¡Error! No se encontró ninguna coincidencia en YouTube.")




### CREAR ARCHIVO CSV

with open(f"informe_{brand}_{model}.csv", mode='w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    
    writer.writerow(["Marca", brand])
    writer.writerow(["Modelo", model])
    
    if error_404_ac == False:
        text_version="Versiones"
        versiones_line = []
        versiones_line.insert(0, text_version)
        for version_ in all_versions:
            versiones_line.append(version_)
        writer.writerow(versiones_line)

        text_pesos = "Precio lista $"
        pesos_line = []
        pesos_line.insert(0, text_pesos)
        for pesos_ in prices_value_converted:
            pesos_line.append("$" + str(pesos_))
        writer.writerow(pesos_line)

        text_dolares = "Precio lista u$d"
        dolares_line = []
        dolares_line.insert(0, text_dolares)
        for dolares_ in prices_value_converted_dolars:
            dolares_line.append("u$d" + str(dolares_))
        writer.writerow(dolares_line)
    else:
        writer.writerow(["Versiones", "No Encontrado"])
        writer.writerow(["Precio lista $", "No Encontrado"])
        writer.writerow(["Precio lista u$d", "No Encontrado"])

    writer.writerow(["Precio promedio meli $", "$" + str(avg_price_meli)])
    writer.writerow(["Precio promedio meli u$d", "u$d" + str(avg_price_meli_dolar)])

    writer.writerow(["Cotizacion dolar Blue", "$" + str(dolar_blue_value)])

    if video_find:
        writer.writerow(["Link test youtube", video_url])
    else:
        writer.writerow(["Link test youtube", "No Encontrado"])


print("Archivo CSV creado exitosamente.")



input("presione enter para finalizar")
he.kill_browser()
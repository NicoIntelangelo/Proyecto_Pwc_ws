import time
import helium as he

#BUSCAR AUTO EN MERCADO LIBRE Y CALCULAR SU PRECIO PROMEDIO
marca = str(input("seleccione la marca: "))
model = str(input("seleccione el modelo: "))

he.start_chrome(f"https://autos.mercadolibre.com.ar/{marca}/{model}/0-km/2023/")

time.sleep(5)

precios = he.find_all(he.S(".andes-money-amount__fraction"))

suma = 0

for i in range(0,30):
    #print(precios[i].web_element.text)
    clear_num = int(precios[i].web_element.text.replace(".", ""))
    #print(clear_num)
    suma = suma + clear_num

avg = int(suma/30)


## COTIZACION DOLAR BLUE VENTA
he.go_to("https://dolarhoy.com/cotizaciondolarblue")

dolar_blue_venta = he.find_all(he.S("//html/body/div[3]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]"))


if len(dolar_blue_venta ) > 0 :
    for value in dolar_blue_venta :
        value = value.web_element.text.split(".")[0]
        value = int(value.split("$")[1])



print("$",avg)
print("u$d",int(avg/value))

# BUSCAR EN AUTOCOSMOS
if len(model) >= 1:
    model_ac = model.replace(" ", "-")

he.go_to(f"https://www.autocosmos.com.ar/catalogo/vigente/{marca}/{model_ac}")

# #DESCARGAR IMAGEN
# time.sleep(5)

# first_image = he.find_all(he.S("body main article section figure picture img"))[0]

# first_image_src = first_image.web_element.get_attribute("src")

# import requests
# response = requests.get(first_image_src)

# if response.status_code == 200:
#     with open("nombre_imagen.jpg", "wb") as f:
#         f.write(response.content)
#     print("Imagen descargada exitosamente.")
# else:
#     print("Error al descargar la imagen.")

#BUSCAR VERSIONES 
versiones = he.find_all(he.S("body section div div table tbody tr td a"))

#print(versiones)
for i in range(0,len(versiones),2):
    print(versiones[i].web_element.text)
    


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
video_titles = he.find_all(he.S("#video-title"))

# if len(model) >= 1:
#     model_yt = model.replace(" ", "")


not_find = True

for titles in video_titles:
    if marca.lower() and model.lower() in titles.web_element.text.lower():
        he.click(titles)
        not_find = False
        break

if not_find:
    print("¡Error! No se encontró ninguna coincidencia en YouTube.")




## SKIP ADD YOUTUBE
time.sleep(8)

skip_add = he.find_all(he.S("//html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[20]/div/div[3]/div/div[2]/span/button"))


if len(skip_add) > 0 :
    for skip_button in skip_add:
        he.click(skip_button)



input("presione enter para finalizar")
he.kill_browser()
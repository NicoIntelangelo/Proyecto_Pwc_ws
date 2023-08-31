#DESCARGAR IMAGEN
time.sleep(5)

first_image = he.find_all(he.S("body main article section figure picture img"))[0]

first_image_src = first_image.web_element.get_attribute("src")

import requests
response = requests.get(first_image_src)

if response.status_code == 200:
    with open("nombre_imagen.jpg", "wb") as f:
        f.write(response.content)
    print("Imagen descargada exitosamente.")
else:
    print("Error al descargar la imagen.")



## SKIP ADD YOUTUBE
time.sleep(8)

skip_add = he.find_all(he.S("//html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[20]/div/div[3]/div/div[2]/span/button"))


if len(skip_add) > 0 :
    for skip_button in skip_add:
        he.click(skip_button)

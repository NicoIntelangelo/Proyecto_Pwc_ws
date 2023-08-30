import time
import helium as he

he.start_chrome("https://dolarhoy.com/cotizaciondolarblue")

dolar_blue_venta = he.find_all(he.S("//html/body/div[3]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]"))


if len(dolar_blue_venta ) > 0 :
    for value in dolar_blue_venta :
        value = value.web_element.text.split(".")[0]
        value = int(value.split("$")[1])
        
        
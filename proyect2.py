import time
import helium as he

he.start_chrome("https://www.youtube.com/@MatiasAnticoTV/videos")

video_titles = he.find_all(he.S("#video-title"))


time.sleep(5)

for titles in video_titles:
    if "ford" and "ranger" not in titles.web_element.text.lower():
        continue
    he.click(titles)
    break

time.sleep(7)

skip_add = he.find_all(he.S("//html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[20]/div/div[3]/div/div[2]/span/button"))


if len(skip_add) > 0 :
    for skip_button in skip_add:
        he.click(skip_button)
        






input("presione enter para finalizar")
he.kill_browser()
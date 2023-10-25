from bs4 import BeautifulSoup
import requests
import re


def car_list (form_data) -> set:
    car_id_list = set()

    url = 'https://crautos.com/autosusados/searchresults.cfm'
    server = requests.post(url, data=form_data)
    output = BeautifulSoup(server.content,"html.parser")
    #print (output)
    car_web_section = output.find_all("section", {"class": "content"})
    car_web_list = car_web_section[0].find_all("a")
    #print(car_web_list)
    for car_web in car_web_list:
        link = car_web.get("href")
        if bool(re.match("https:\/\/crautos\.com\/autosusados\/cardetail\.cfm\?c\=[0-9]*",link)):
            car_id_list.add(re.sub("https:\/\/crautos\.com\/autosusados\/cardetail\.cfm\?c\=","",link))
    return car_id_list


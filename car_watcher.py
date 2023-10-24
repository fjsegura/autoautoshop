from bs4 import BeautifulSoup
import requests
import re
import car_garage


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

#form_data = {   "brand": "4",
                        #"financed": "0",
                        #"yearfrom": "1960",
                        #"yearto": "2020",
                        #"pricefrom": "100000",
                        #"priceto": "200000000",
                        #"style": "00",
                        #"province": "0",
                        #"doors": "0",
                        #"orderby": "0",
                        #"newused": "0",
                        #"fuel": "0",
                        #"trans": "0",
                        #"recibe": "0",
                        #"modelstr": "",
                        #}
#print(car_list(form_data))
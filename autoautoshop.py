from bs4 import BeautifulSoup
import requests
import json
import time
import param_setup
import car_garage
import car_watcher

def main():
    #Extract param values
    brand_dict,style_dict,province_dict,year_set,price_set,trans_dict,fuel_dict,doors_dict = param_setup.extract_param_values()
    #Read and verify config file
    search_brand_list = {"Suzuki":["Sidekick","Sidekick sport"],"Geo":["Tracker"]}
    search_style_list = ["Todo Terreno 4x4","Todo Terreno 4x2"]

    #Do the quearies
    car_garage_data = car_garage.car_garage_class("prueba")
    #car_garage_data = car_garage_data.car_data()

    for style in search_style_list:
        for brand in search_brand_list:
            for model in search_brand_list[brand]:
                form_data = {   "brand": brand_dict[brand],
                            "financed": "0",
                            "yearfrom": "1960",
                            "yearto": "2020",
                            "pricefrom": "100000",
                            "priceto": "200000000",
                            "style": style_dict[style],
                            "province": "0",
                            "doors": "0",
                            "orderby": "0",
                            "newused": "0",
                            "fuel": "0",
                            "trans": "0",
                            "recibe": "0",
                            "modelstr": model,
                            }
                #print(form_data)
                #continue
                car_id_list = car_watcher.car_list(form_data)
                for car_id in car_id_list:
                    car_garage_data.add_car(car_id)
                    time.sleep(1)
    #Filter the results
    car_garage_data.save_csv()
    #Save the results
main()
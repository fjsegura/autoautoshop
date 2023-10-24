from bs4 import BeautifulSoup
import requests
import json
import param_setup


def main():
    #Extract param values
    brand_dict,style_dict,province_dict,year_set,price_set,trans_dict,fuel_dict,doors_dict = param_setup.extract_param_values()
    #Read and verify config file

    #Do the quearies

    #Filter the results

    #Save the results
url = 'https://crautos.com/autosusados/searchresults.cfm'
form_data = {   "brand": "4",
                "financed": "0",
                "yearfrom": "1960",
                "yearto": "2020",
                "pricefrom": "100000",
                "priceto": "200000000",
                "style": "00",
                "province": "0",
                "doors": "0",
                "orderby": "0",
                "newused": "0",
                "fuel": "0",
                "trans": "0",
                "recibe": "0",
                "modelstr": "",
                #"totalads": "",
                #"splitoption": "0",
             }
server = requests.post(url, data=form_data)
output = BeautifulSoup(server.content,"html.parser")
print(output.find())
#with open ("file.html","w") as f:
#    print( output,file=f)
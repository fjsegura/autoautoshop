from bs4 import BeautifulSoup
import requests

def extract_param_values():
    crautosURL = "https://crautos.com/autosusados/"
    page = requests.get(crautosURL)
    soup = BeautifulSoup(page.content,"html.parser")
    #results = soup.find(id="sf")
    atribute_list = ["brand","style","province","yearto","priceto","trans","fuel","doors"]
    brand_dict = dict()
    style_dict = dict()
    province_dict = dict()
    trans_dict = dict()
    fuel_dict = dict()
    doors_dict = dict()
    year_set = set()
    price_set = set()
    for atribute in atribute_list:
        param_dict = dict()
        extract_params = soup.find_all(attrs={"name" : atribute})
        option_list = extract_params[0].find_all("option")
        for option_name_value_pair in option_list:
            param_dict.update({option_name_value_pair.get_text():option_name_value_pair.get("value")})
        match atribute:
            case "brand":
                brand_dict = param_dict
            case "style":
                style_dict = param_dict
            case "province":
                province_dict = param_dict
            case "trans":
                trans_dict = param_dict
            case "fuel":
                fuel_dict = param_dict
            case "doors":
                doors_dict = param_dict
            case "newused":
                newused_dict = param_dict
            case "yearto":
                year_set = set(param_dict.keys())
            case "priceto":
                price_set = set(param_dict.values())
    return brand_dict,style_dict,province_dict,year_set,price_set,trans_dict,fuel_dict,doors_dict


#print(extract_param_values())
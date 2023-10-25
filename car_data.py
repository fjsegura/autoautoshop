import requests
import pandas as pd
import re

class car():
    def __init__(self,car_id) -> None:
        car_url = "https://crautos.com/autosusados/extract.cfm?c={}".format(car_id)
        page = requests.get(car_url)
        general_data_tables = pd.read_html(page.text)
        general_data = general_data_tables.pop()
        general_data = general_data.drop(general_data.columns[[0]], axis=1)
        equipment_flag = False
        last_line = False
        self.equipment = set()
        for index,row in general_data.iterrows() :
            row = list(row)
            match row[0]:
                case "Marca:":
                    self.brand = row[1]
                case "Modelo:":
                    self.model = row[1]
                case "Cilindrada:":
                    self.engine = row[1].replace(",","")
                case "Estilo:":
                    self.style = row[1]
                case "Año:":
                    self.year = row[1]
                case "Precio:":
                    self.price = row[1].replace(",","")
                case "Estado:":
                    self.status = row[1]
                case "Color  Exterior:":
                    self.ext_color = row[1]
                case "Color  Interior:":
                    self.int_color = row[1]
                case "Combustible:":
                    self.fuel = row[1]
                case "Transmisión:":
                    self.transmision = row[1]
                case "Kilometraje:":
                    self.odometer = row[1]
                case "Está  inscrito:":
                    self.inscribed = row[1]
                case "#  de puertas:":
                    self.door_amount = row[1]
                case "Provincia:":
                    self.region = row[1]
                case "Ingresó:":
                    self.registered_on = row[1]
                case "Equipamiento":
                    equipment_flag = True
                    continue
                case "Vende":
                    equipment_flag = False
                    continue
                case "Nombre:":
                    self.vendor_name = row[1]
                    continue
                case "Teléfono:":
                    self.vendor_number = row[1]
                    last_line = True
                    continue
            if equipment_flag:
                if str(row[1]) == "nan":
                    continue
                self.equipment.add(str(row[1]).replace(".",""))
            if last_line:
                self.vendor_comment = row[1].replace(",","")
                break
    
    def return_equipment(self):
        return_list = list(self.equipment)
        return_list.sort()
        return return_list
    def return_csv_titles(self):
        variables = vars(self)
        return_str = ""
        variables_keys_list = list(variables.keys())
        variables_keys_list.sort()
        for key_name in variables_keys_list:
            return_str += "{},".format(key_name)
        return re.sub(",$","",return_str)

    def return_csv_format(self):
        variables = vars(self)
        return_str = ""
        variables_keys_list = list(variables.keys())
        variables_keys_list.sort()
        for key_name in variables_keys_list:
            if type(variables[key_name]) == str:
                data = re.sub(";","",variables[key_name])
            else:
                sort_list = list(variables[key_name])
                sort_list.sort()
                ','.join(map(str, sort_list))
                data = ';'.join(map(str, sort_list))
            return_str += "{},".format(data)
        return re.sub(",$","",return_str)

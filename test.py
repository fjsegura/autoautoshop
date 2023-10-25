import unittest
import car_data
import car_garage

class TestCarGarage(unittest.TestCase):
      car_storage = car_garage.car_garage_class("test")
      car_id = "41884859"
      def test_car_garage_data(self):
            self.car_storage.add_car(self.car_id)
            print(self.car_storage.return_csv_str())
class TestCarDataExtract(unittest.TestCase):
    car_id = "41884859"
    equipment_list = ['Aire acondicionado', 'Aire acondicionado climatizado', 'Alarma', 'Aros de lujo', 'Bluetooth', 'Bolsa de aire', 'Caja de cambios dual', 'Cierre central', 'Computadora de viaje', 'Control de radio en el volante', 'Control electrónico de estabilidad', 'Cámara de retroceso', 'Desempañador trasero', 'Dirección hidráulica', 'Disco compacto', 'Espejos Eléctricos', 'Frenos ABS', 'Halógenos', 'Llave inteligente/botón de arranque', 'Luces de Xenón/Bixenón', 'Monitor de presión de llantas', 'RTV al día', 'Radio con USB/AUX', 'Sensores de retroceso', 'Tapicería de cuero', 'Turbo', 'Vidrios Eléctricos', 'Vidrios tintados', 'Volante ajustable', 'Volante multifuncional']
    csv_titles = "brand,door_amount,engine,equipment,ext_color,fuel,inscribed,int_color,model,odometer,price,region,registered_on,status,style,transmision,vendor_comment,vendor_name,vendor_number,year"
    csv_format = "Land Rover,Land Rover,5,5,3,000 cc,3,000 cc,Aire acondicionado;Aire acondicionado climatizado;Alarma;Aros de lujo;Bluetooth;Bolsa de aire;Caja de cambios dual;Cierre central;Computadora de viaje;Control de radio en el volante;Control electrónico de estabilidad;Cámara de retroceso;Desempañador trasero;Dirección hidráulica;Disco compacto;Espejos Eléctricos;Frenos ABS;Halógenos;Llave inteligente/botón de arranque;Luces de Xenón/Bixenón;Monitor de presión de llantas;RTV al día;Radio con USB/AUX;Sensores de retroceso;Tapicería de cuero;Turbo;Vidrios Eléctricos;Vidrios tintados;Volante ajustable;Volante multifuncional,AZUL,AZUL,Diesel,Diesel,SI,SI,NEGRO,NEGRO,DISCOVERY GRAPHITE,DISCOVERY GRAPHITE,141000 Kms.,141000 Kms.,¢ 21,000,000,¢ 21,000,000,San José,San José,22 de Octubre del 2023,22 de Octubre del 2023,Excelente,Excelente,Todo Terreno 4x4,Todo Terreno 4x4,Automática,Automática,Impecable,Impecable,RODOLFO TRAUBE,RODOLFO TRAUBE,8846-4075,8846-4075,2016,2016"
    test_car = car_data.car(car_id)

    def test_car_init_brand(self):
          self.assertEqual(self.test_car.brand, "Land Rover")
          
    def test_car_init_model(self):
          self.assertEqual(self.test_car.model, "DISCOVERY GRAPHITE")
          
    def test_car_init_engine(self):
          self.assertEqual(self.test_car.engine, "3,000 cc")

    def test_car_init_style(self):
          self.assertEqual(self.test_car.style, "Todo Terreno 4x4")
          
    def test_car_init_year(self):
          self.assertEqual(self.test_car.year, "2016")

    def test_car_init_price(self):
          self.assertEqual(self.test_car.price, "¢ 21,000,000")
          
    def test_car_init_status(self):
          self.assertEqual(self.test_car.status, "Excelente")

    def test_car_init_ext_color(self):
          self.assertEqual(self.test_car.ext_color, "AZUL")

    def test_car_init_int_color(self):
          self.assertEqual(self.test_car.int_color, "NEGRO")

    def test_car_init_fuel(self):
          self.assertEqual(self.test_car.fuel, "Diesel")
          
    def test_car_init_transmision(self):
          self.assertEqual(self.test_car.transmision, "Automática")

    def test_car_init_odometer(self):
          self.assertEqual(self.test_car.odometer, "141000 Kms.")
          
    def test_car_init_inscribed(self):
          self.assertEqual(self.test_car.inscribed, "SI")
          
    def test_car_init_door_amount(self):
          self.assertEqual(self.test_car.door_amount, "5")
          
    def test_car_init_region(self):
          self.assertEqual(self.test_car.region, "San José")
          
    def test_car_init_registered_on(self):
          self.assertEqual(self.test_car.registered_on, "22 de Octubre del 2023")
          
    def test_car_init_vendor_name(self):
          self.assertEqual(self.test_car.vendor_name, "RODOLFO TRAUBE")
          
    def test_car_init_vendor_number(self):
          self.assertRegex(self.test_car.vendor_number, r"[0-9]{1}\-[0-9]{4}")
          
    def test_car_init_vendor_comment(self):
          self.assertEqual(self.test_car.vendor_comment, "Impecable")
    
    def test_car_init_equipment_set(self):
          for equi in self.equipment_list:
                self.assertIn (equi,self.test_car.equipment)

    def test_car_init_equipment_list(self):
          self.assertEqual (self.equipment_list,self.test_car.return_equipment())

    def test_car_init_csv_titles(self):
          self.assertEqual (self.test_car.return_csv_titles(),self.csv_titles)

    def test_car_init_equipment_list(self):
          self.assertEqual (self.test_car.return_csv_format(),self.csv_format)

if __name__ == '__main__':
    unittest.main()
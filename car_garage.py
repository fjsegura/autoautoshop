import car_data

class car_garage_class():
    def __init__(self,name):
        self.name = name
        self.car_storage = dict()
    def add_car (self,car_id):
        if car_id not in self.car_storage:
            car = car_data.car(car_id)
            self.car_storage.update({car_id:car})
    def return_csv_str(self):
        print_str =""#car_data.car.return_csv_titles() 
        #with open("test.csv","w") as f:
        #    print(print_str,file=f)
        first_line = True
        for car in self.car_storage:
            if first_line:
                print_str = print_str +self.car_storage[car].return_csv_titles()  
                first_line =False  
            print_str = print_str +"\n"+self.car_storage[car].return_csv_format()
        return print_str
        
    def save_csv(self):
        print_str =car_data.car.return_csv_titles() 
        with open("test.csv","w") as f:
            print(print_str,file=f)
            for car in self.car_storage:
                print(self.car_storage[car].return_csv_format(),file=f)


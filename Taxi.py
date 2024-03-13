class Taxi:
    def __init__(self, name, phone_number):
        self.__name = name
        self.__phone_number = phone_number
        self.__car_list = []

    @property
    def get_name (self):
        return self.__name
    
    @property
    def get_phone (self):
        return self.__phone_number

    @property
    def get_car_list (self):
        return self.__car_list
    
    #เพิ่มรถเข้า List
    def add_car_to_list (self, car):
        self.__car_list.append(car)
        return self
    
    #Seach หารถที่ว่างพร้อมให้บริการและส่งคืนเป็น list 
    @property
    def seach_available_car (self):
        car_list = []
        for car in self.__car_list:
            if car.get_travel_date == None:
                car_list.append(car)
        return car_list
    
    def search_car_from_phone(self, phone):
        for car in self.__car_list:
            if car.get_phone_number == phone:
                return car
        return None
    
class Car:
    def __init__(self, phone_number):
        self.__phone_number = phone_number
        self.__travel_type = None
        self.__travel_date = None
        self.__pickup_location = None
        self.__destination_location = None
    
    @property
    def get_phone_number (self):
        return self.__phone_number
    
    @property
    def get_travel_type (self):
        return self.__travel_type
    
    @property
    def get_travel_date (self):
        return self.__travel_date

    
    @property
    def get_pickup_location (self):
        return self.__pickup_location
    
    @property
    def get_destination_location (self):
        return self.__destination_location
    
    def set_travel_type (self, travel_type):
        self.__travel_type = travel_type
        return self
    
    def set_travel_date (self, travel_date):
        self.__travel_date = travel_date
        return self
    
    def set_pickup_location (self, pickup_location):
        self.__pickup_location = pickup_location
        return self
    
    def set_destination_location (self, destination_location):
        self.__destination_location = destination_location
        return self
    

class Seadard(Car):
    def __init__(self, phone_number, head_count, price):
        Car.__init__(self, phone_number)
        self.__car_type = "Seadard"
        self.__head_count = head_count
        self.__price = price

    @property
    def get_car_type(self):
        return self.__car_type

    @property
    def get_head_count (self):
        return self.__head_count
    
    @property
    def get_price (self):
        return self.__price

class Suv(Car):
    def __init__(self, phone_number, head_count, price):
        Car.__init__(self, phone_number)
        self.__car_type = "Suv"
        self.__head_count = head_count
        self.__price = price

    @property
    def get_car_type(self):
        return self.__car_type

    @property
    def get_head_count (self):
        return self.__head_count
    
    @property
    def get_price (self):
        return self.__price      

class Private(Car):
    def __init__(self, phone_number, head_count, price):
        Car.__init__(self, phone_number)
        self.__car_type = "Private"
        self.__head_count = head_count
        self.__price = price

    @property
    def get_car_type(self):
        return self.__car_type

    @property
    def get_head_count (self):
        return self.__head_count
    
    @property
    def get_price (self):
        return self.__price






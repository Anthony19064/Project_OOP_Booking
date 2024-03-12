class Control:
    def __init__(self):
        self.__hotel_list = []
        self.__taxi_list = []
        self.__account_list = []

    @property
    def get_hotel_list(self):
        self.__hotel_list.sort(key=lambda x: x._Hotel__name)
        return self.__hotel_list
    
    @property
    def get_taxi_list(self):
        self.__taxi_list.sort(key=lambda x: x._Taxi__name)
        return self.__taxi_list

    @property
    def get_account_list(self):
        return self.__account_list
    
    def add_hotel(self, hotel):
        self.__hotel_list.append(hotel)
        return self
    
    def add_taxi(self, taxi):
        self.__taxi_list.append(taxi)
        return self
    
    def add_account(self, account):
        self.__account_list.append(account)
        return self
    
    #หาโรงแรมจากชื่อโรงแรมคืนเป็น instance
    def seach_hotel_from_name(self, hotel_name):
        for hotel in self.__hotel_list:
            if (hotel.get_name).lower() == hotel_name.lower():
                return hotel
        return None

    #หาโรงแรมจากจังหวัดคืนเป็น list
    def seach_hotel_from_location(self, hotel_location):
        list_hotel = []
        for hotel in self.__hotel_list:
            if (hotel.get_location).lower() == hotel_location.lower():
                list_hotel.append(hotel)
        return list_hotel
    
    #หาแท็กซี่จากชื่อบริษัทแท็กซี่คืนเป็น instance
    def seach_taxi(self, taxi_name):
        for taxi in self.__taxi_list:
            if (taxi.get_name).lower() == taxi_name.lower():
                return taxi
        return None
    
    #หาแอคเค้าจากชื่อแอคเค้าคืนเป็น instance
    def seach_account(self, account_name):
        for account in self.__account_list:
            if account.get_name == account_name:
                return account
        return None

        
class Account:
    def __init__(self, name, password, mail):
        self.__name = name
        self.__password = password
        self.__mail = mail
        self.__transaction = []
    
    @property    
    def get_name(self):
        return self.__name
    
    @property
    def get_password(self):
        return self.__password
    
    @property
    def get_mail(self):
        return self.__mail
    
    def add_transaction (self, transaction):
        self.__transaction.append(transaction)
        return self
    
    @property
    def get_transaction (self):
        return self.__transaction
    
class Admin(Account):
    def __init__(self, name, password, mail):
        Account.__init__(self, name, password, mail)
        self.__permisstion = "Root"

    @property
    def get_permisstion (self):
        return self.__permisstion

class User(Account):
    def __init__(self, name, password, mail):
        Account.__init__(self, name, password, mail)
        self.__permisstion = "User"

    @property
    def get_permisstion (self):
        return self.__permisstion

    
class Transection:
    id = 0
    def __init__(self, type):
        self.__id = Transection.id
        Transection.id += 1
    
    @property
    def get_id (self):
        return self.__id

    @property
    def get_type (self):
        return self.__type

class Transection_hotel(Transection):
    def __init__(self, hotel_name, room, date_in, date_out, price, head_count, name):
        Transection.__init__(self, type)
        self.__type = "Hotel"
        self.__hotel_name = hotel_name
        self.__room = room
        self.__date_in = date_in
        self.__date_out = date_out
        self.__price = price
        self.__headcount = head_count
        self.__name = name

    @property
    def get_type(self):
        return self.__type
    
    @property
    def get_hotel_name(self):
        return self.__hotel_name
    
    @property
    def get_room(self):
        return self.__room
    
    @property
    def get_date_in(self):
        return self.__date_in
    
    @property
    def get_date_out(self):
        return self.__date_out

    @property
    def get_price(self):
        return self.__price
    
    @property
    def get_headcount(self):
        return self.__headcount

    @property
    def get_name(self):
        return self.__name

class Transection_taxi(Transection):
    def __init__(self, taxi_name, taxi_type, pickup_location, destination_location, price, head_count, name):
        Transection.__init__(self, type)
        self.__type = "Taxi"
        self.__taxi_name = taxi_name
        self.__taxi_type = taxi_type
        self.__pickup_location = pickup_location
        self.__destination_location = destination_location
        self.__price = price
        self.__headcount = head_count
        self.__name = name
    
    @property
    def get_type(self):
        return self.__type
    
    @property
    def get_taxi_name(self):
        return self.__taxi_name
    
    @property
    def get_taxi_type(self):
        return self.__taxi_type
    
    @property
    def get_pickup_location(self):
        return self.__pickup_location
    
    @property 
    def get__destination_location(self):
        return self.__destination_location
     
    @property
    def get_price(self):
        return self.__price
    
    @property
    def get_headcount(self):
        return self.__headcount

    @property
    def get_name(self):
        return self.__name
        
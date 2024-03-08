class Hotel:
    def __init__(self, location, name):
        self.__location = location
        self.__name = name
        self.__room_list = []
        

    #เพิ่มห้องเข้า list Hotel
    def add_room_to_list (self, room):
        self.__room_list.append(room)
        return self

    # ค้นหาห้องที่ว่าง
    @property
    def search_available_room(self):
        room_list = []
        for room in self.__room_list:
            if room.get_date_in == None and room.get_date_out == None:
                room_list.append(room)
        return room_list
    
    def search_room(self, room_number):
        for room in self.__room_list:
            if room.get_room_number == room_number:
                return room

    @property
    def get_room_list (self):
        return self.__room_list
    
    @property
    def get_location (self):
        return self.__location
    
    @property
    def get_name (self):
        return self.__name

class Room:
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__date_in = None
        self.__date_out = None
    
    @property
    def get_date_in (self):
        return self.__date_in

    @property
    def get_date_out (self):
        return self.__date_out
    @property
    def get_room_number (self):
        return self.__room_number
        
    #เพิ่มวันที่เข้าโรงแรม
    def set_date_in (self, date_in):
        self.__date_in = date_in

    #เพิ่มวันที่ออกโรงแรม
    def set_date_out (self, date_out):
        self.__date_out = date_out
    


class Standard(Room):
    def __init__(self, room_number , head_count , price , bed):
        Room.__init__(self, room_number)
        self.__type_room = "Standard"
        self.__head_count = head_count
        self.__price = price
        self.__bed = bed
            
    @property
    def get_type_room(self):
        return self.__type_room

    @property
    def get_head_count(self):
        return self.__head_count
    
    @property
    def get_price(self):
        return self.__price
    
    @property
    def get_bed(self):
        return self.__bed

class Deluxe(Room):
    def __init__(self, room_number, head_count, price, bed):
        Room.__init__(self, room_number)
        self.__type_room = "Deluxe"
        self.__head_count = head_count
        self.__price = price
        self.__bed = bed
            
    @property
    def get_type_room(self):
        return self.__type_room
    
    @property
    def get_head_count(self):
        return self.__head_count
    
    @property
    def get_price(self):
        return self.__price
    
    @property
    def get_bed(self):
        return self.__bed

class Superior(Room):
    def __init__(self, room_number, head_count, price, bed):
        Room.__init__(self, room_number)
        self.__type_room = "Superior"
        self.__head_count = head_count
        self.__price = price
        self.__bed = bed
    
    @property
    def get_type_room(self):
        return self.__type_room

    @property
    def get_head_count(self):
        return self.__head_count
    
    @property
    def get_price(self):
        return self.__price
    
    @property
    def get_bed(self):
        return self.__bed





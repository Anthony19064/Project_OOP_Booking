from instance import *
creat_instance()
creat_account('yotha','12345')

hotel_list = control.get_hotel_list
taxi_list = control.get_taxi_list
account_list = control.get_account_list

hotel_list.sort(key=lambda x: x._Hotel__name)

hotel = control.seach_hotel_from_name("Amora Thapae")
room = hotel.search_room('801')
print(room)

# list = control.seach_hotel_from_location('bangkok')
# print(list)

# for hotel in list:
#     print(hotel.get_name)

# hotel = control.seach_hotel_from_name('Lit Bangkok')
# print(hotel.get_name)
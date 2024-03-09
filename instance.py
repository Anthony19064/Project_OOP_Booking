from Taxi import *
from Hotel import *
from Main import *

control = Control()

def creat_instance():

    #สร้าง Taxi1, Taxi2, Taxi3
    Taxi1 = Taxi('Taxi Company','0900000001')
    Taxi2 = Taxi('Taxi Siam inter Company','0900000002')
    Taxi3 = Taxi('Taxi bangkok','0900000003')

    # สร้าง hotel1 , hotel2 , hotel3
    hotel1  = Hotel("กรุงเทพ","Lit Bangkok")
    hotel2  = Hotel("กรุงเทพ","Oakwood")
    hotel3  = Hotel("กรุงเทพ","Baiyoke Sky")
    hotel4  = Hotel("กรุงเทพ","The Quartier")
    hotel5  = Hotel("เชียงใหม่","Centara Chiang Mai")
    hotel6  = Hotel("เชียงใหม่","The Opium")
    hotel7  = Hotel("เชียงใหม่","Glory Boutique")
    hotel8  = Hotel("เชียงใหม่","Amora Thapae")
    hotel9  = Hotel("ชลบุรี","Bangsean")
    hotel10 = Hotel("ชลบุรี","Karin")
    hotel11 = Hotel("ชลบุรี","Citadines Grand Central")
    hotel12 = Hotel("ชลบุรี","Madera Residence")
    hotel13 = Hotel("ภูเก็ต","The Blanket")
    hotel14 = Hotel("ภูเก็ต","Blue Carina")
    hotel15 = Hotel("ภูเก็ต","Blu Monkey")
    hotel16 = Hotel("ภูเก็ต","Seabed Grand")
    hotel17 = Hotel("ขอนแก่น","Nadee 10")
    hotel18 = Hotel("ขอนแก่น","Romantic")
    hotel19 = Hotel("ขอนแก่น","Sirin")
    hotel20 = Hotel("ขอนแก่น","Le cassia")
    hotel21 = Hotel("ระยอง","Star Convention")
    hotel22 = Hotel("ระยอง","Novotel Rayong Star Centre")
    hotel23 = Hotel("ระยอง","Hotel Fuse Rayong")
    hotel24 = Hotel("ระยอง","Phavina Hotel Rayong")
    
    #เพิ่มรถเข้า Taxi1
    Taxi1.add_car_to_list(Seadard('081', 4, 800)).add_car_to_list(Seadard('082', 4, 750)).add_car_to_list(Seadard('083', 3, 700))
    Taxi1.add_car_to_list(Suv('071', 6, 1000)).add_car_to_list(Suv('072', 5, 900)).add_car_to_list(Suv('0700000003', 7, 1300))
    Taxi1.add_car_to_list(Private('061', 10, 3000)).add_car_to_list(Private('062', 12, 3500)).add_car_to_list(Private('063', 7, 4500))

    #เพิ่มรถเข้า Taxi2
    Taxi2.add_car_to_list(Seadard('051', 4, 1000)).add_car_to_list(Seadard('052', 4, 900)).add_car_to_list(Seadard('053', 3, 800))
    Taxi2.add_car_to_list(Suv('041', 6, 1200)).add_car_to_list(Suv('042', 5, 1000)).add_car_to_list(Suv('043', 7, 1500))
    Taxi2.add_car_to_list(Private('031', 10, 5000)).add_car_to_list(Private('032', 12, 7000)).add_car_to_list(Private('033', 7, 6000))

    #เพิ่มรถเข้า Taxi3
    Taxi3.add_car_to_list(Seadard('021', 4, 1500)).add_car_to_list(Seadard('022', 4, 1600)).add_car_to_list(Seadard('023', 3, 1800))
    Taxi3.add_car_to_list(Suv('011', 6, 2000)).add_car_to_list(Suv('012', 5, 1800)).add_car_to_list(Suv('013', 7, 2000))
    Taxi3.add_car_to_list(Private('001', 10, 7000)).add_car_to_list(Private('002', 12, 10000)).add_car_to_list(Private('003', 7, 9000))

    #เพิ่มห้องเข้า hotel1
    hotel1.add_room_to_list(Standard(101 ,2, 1500, "Single")).add_room_to_list(Deluxe(102, 6, 6000, "King")).add_room_to_list(Superior(103,4,3500,"Twin"))      

    #เพิ่มห้องเข้า hotel2
    hotel2.add_room_to_list(Standard(301, 2,1900, "Single")).add_room_to_list(Deluxe(302, 6, 5500, "King")).add_room_to_list(Superior(303,4, 2900, "Twin")) 

    #เพิ่มห้องเข้า hotel3
    hotel3.add_room_to_list(Standard(201, 2, 2000, "Single")).add_room_to_list(Deluxe(202, 6, 4200, "King")).add_room_to_list(Superior(203, 4, 3600, "Twin"))   

    #เพิ่มห้องเข้า hotel4
    hotel4.add_room_to_list(Standard(401, 2, 2600, "Single")).add_room_to_list(Deluxe(402, 6, 7000, "King")).add_room_to_list(Superior(403, 4, 3100, "Twin"))

    #เพิ่มห้องเข้า hotel5
    hotel5.add_room_to_list(Standard(501, 2, 1600, "Single")).add_room_to_list(Deluxe(502, 6, 5500, "King")).add_room_to_list(Superior(503, 4, 2800, "Twin"))

    #เพิ่มห้องเข้า hotel6
    hotel6.add_room_to_list(Standard(601, 2, 1900, "Single")).add_room_to_list(Deluxe(602, 6, 4000, "King")).add_room_to_list(Superior(603, 4, 2500, "Twin"))   

    #เพิ่มห้องเข้า hotel7
    hotel7.add_room_to_list(Standard(701, 2, 2000, "Single")).add_room_to_list(Deluxe(702, 6, 4500, "King")).add_room_to_list(Superior(703, 4, 3000, "Twin"))

    #เพิ่มห้องเข้า hotel8
    hotel8.add_room_to_list(Standard(801, 2, 1200, "Single")).add_room_to_list(Deluxe(802, 6, 5200, "King")).add_room_to_list(Superior(803, 4, 2700, "Twin"))

    #เพิ่มห้องเข้า hotel9
    hotel9.add_room_to_list(Standard(901, 2, 1900, "Single")).add_room_to_list(Deluxe(902, 6, 6000, "King")).add_room_to_list(Superior(903, 4, 3200, "Twin"))

    #เพิ่มห้องเข้า hotel10
    hotel10.add_room_to_list(Standard(401, 2, 1800, "Single")).add_room_to_list(Deluxe(402, 6, 4000, "King")).add_room_to_list(Superior(403, 4, 3000, "Twin"))

    #เพิ่มห้องเข้า hotel11
    hotel11.add_room_to_list(Standard(301, 2, 1500, "Single")).add_room_to_list(Deluxe(302, 6, 3900, "King")).add_room_to_list(Superior(303, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel12
    hotel12.add_room_to_list(Standard(101, 2, 1700, "Single")).add_room_to_list(Deluxe(102, 6, 4000, "King")).add_room_to_list(Superior(103, 4, 3500, "Twin"))

    #เพิ่มห้องเข้า hotel13
    hotel13.add_room_to_list(Standard(101, 2, 2000, "Single")).add_room_to_list(Deluxe(102, 6, 4500, "King")).add_room_to_list(Superior(103, 4, 3600, "Twin"))

    #เพิ่มห้องเข้า hotel14
    hotel14.add_room_to_list(Standard(301, 2, 1900, "Single")).add_room_to_list(Deluxe(302, 6, 6200, "King")).add_room_to_list(Superior(303, 4, 3700, "Twin"))

    #เพิ่มห้องเข้า hotel15
    hotel15.add_room_to_list(Standard(201, 2, 1800, "Single")).add_room_to_list(Deluxe(202, 6, 6000, "King")).add_room_to_list(Superior(203, 4, 3500, "Twin"))

    #เพิ่มห้องเข้า hotel16
    hotel16.add_room_to_list(Standard(401, 2, 1800, "Single")).add_room_to_list(Deluxe(402, 6, 5800, "King")).add_room_to_list(Superior(403, 4, 3800, "Twin"))

    #เพิ่มห้องเข้า hotel17
    hotel17.add_room_to_list(Standard(401, 2, 1900, "Single")).add_room_to_list(Deluxe(402, 6, 4900, "King")).add_room_to_list(Superior(403, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel18
    hotel18.add_room_to_list(Standard(401, 2, 2000, "Single")).add_room_to_list(Deluxe(402, 6, 5600, "King")).add_room_to_list(Superior(403, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel19
    hotel19.add_room_to_list(Standard(101, 2, 1900, "Single")).add_room_to_list(Deluxe(102, 6, 4500, "King")).add_room_to_list(Superior(103, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel20
    hotel20.add_room_to_list(Standard(301, 2, 1800, "Single")).add_room_to_list(Deluxe(302, 6, 5100, "King")).add_room_to_list(Superior(303, 4, 3200, "Twin"))

    #เพิ่มห้องเข้า hotel21
    hotel21.add_room_to_list(Standard(201, 2, 1900, "Single")).add_room_to_list(Deluxe(202, 6, 4600, "King")).add_room_to_list(Superior(203, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel22
    hotel22.add_room_to_list(Standard(401, 2, 2100, "Single")).add_room_to_list(Deluxe(402, 6, 5000, "King")).add_room_to_list(Superior(403, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel23
    hotel23.add_room_to_list(Standard(401, 2, 1900, "Single")).add_room_to_list(Deluxe(402, 6, 5100, "King")).add_room_to_list(Superior(403, 4, 2500, "Twin"))

    #เพิ่มห้องเข้า hotel24
    hotel24.add_room_to_list(Standard(701, 2, 1500, "Single")).add_room_to_list(Deluxe(702, 6, 6000, "King")).add_room_to_list(Superior(703, 4, 2500, "Twin"))

    #เพิ่ม hotel เข้า list main
    control.add_hotel(hotel1).add_hotel(hotel2).add_hotel(hotel3).add_hotel(hotel4).add_hotel(hotel5).add_hotel(hotel6).add_hotel(hotel7).add_hotel(hotel8).add_hotel(hotel9)
    control.add_hotel(hotel10).add_hotel(hotel11).add_hotel(hotel12).add_hotel(hotel13).add_hotel(hotel14).add_hotel(hotel15).add_hotel(hotel16).add_hotel(hotel17).add_hotel(hotel18)
    control.add_hotel(hotel19).add_hotel(hotel20).add_hotel(hotel21).add_hotel(hotel22).add_hotel(hotel23).add_hotel(hotel24)

    #เพิ่ม taxi เข้า list main
    control.add_taxi(Taxi1).add_taxi(Taxi2).add_taxi(Taxi3)

    #สร้าง account admin และเพิ่ม account admin เข้า list main
    control.add_account( Admin('admin', 'admin', 'booking@gmail.com'))

#ฟังก์ชั่นสร้างแอคเค้า
def creat_account (name, password, mail):
    #สร้าง account จาก parameter name password และเพิ่ม account เข้า list main
    control.add_account(User(name, password, mail))






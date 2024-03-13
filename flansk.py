from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from instance import *
import os


creat_instance()
app = Flask(__name__)
app.secret_key = 'booking'
hotel_list = control.get_hotel_list
taxi_list = control.get_taxi_list
account_list = control.get_account_list



# กำหนดเส้นทางสำหรับโฟลเดอร์รูปภาพ
IMAGE_FOLDER_HOTEL = 'hotel'
IMAGE_FOLDER_HOTEL_BANGKOK = 'hotel_bangkok'
IMAGE_FOLDER_HOTEL_CHIANG_MAI = 'hotel_chiang_mai'
IMAGE_FOLDER_HOTEL_CHONBURI = 'hotel_chonburi'
IMAGE_FOLDER_HOTEL_PHUKET = 'hotel_phuket'
IMAGE_FOLDER_HOTEL_KHON_KAEN = 'hotel_khon_kaen'
IMAGE_FOLDER_HOTEL_RAYONG = 'hotel_rayong'
IMAGE_FOLDER_TAXI = 'taxi'
AMORA_THAPAE = 'room_amorathapae'
BAIYOKE_SKY = 'room_baiyokeskyhotel'
BANGSEAN = 'room_bangseanhotel'
BLU_MONKEY = 'room_blumonkeyhotel'
BLUE_CARINA = 'room_bluecarinahotel'
CENTARA_CHIANG_MAI = 'room_centarachiangmai'
CITADINES_GRAND_CENTRAL = 'room_citadinesgrandcentral'
GLORY_BOUTIQUE = 'room_gloryboutique'
HOTEL_FUSE_RAYONG = 'room_hotelfuserayong'
KARIN = 'room_karinhotel'
LE_CASSIA = 'room_lecassiahotel'
LIT_BANGKOK = 'room_litbangkok'
MADERA_RESIDENCE = 'room_maderaresidence'
NADEE_10 = 'room_nadee10hotel'
NOVOTEL_RAYONG_STAR_CENTRE = 'room_novotelrayongstarcentre'
OAKWOOD = 'room_oakwoodhotel'
PHAVINA_HOTEL_RAYONG = 'room_phavinahotelrayong'
ROMANTIC = 'room_romantichotel'
SEABED_GRAND = 'room_seabedgrandhotel'
SIRIN = 'room_sirinhotel'
STAR_CONVENTION = 'room_starconventionhotel'
THE_BLANKET = 'room_theblankethotel'
THE_OPIUM = 'room_theopium'
THE_QUARTIER = 'room_thequeartierhotel'
TAXI_COMPANY = 'car_taxicompany'
TAXI_SIAM_INTER_COMPANY = 'car_taxisiamintercompany'
TAXI_BANGKOK = 'car_taxibangkok'

@app.route('/images/<path:folder>/<path:image_name>')
def get_image(folder, image_name):
    list_input = ["hotel", "taxi", 'Amora Thapae','Baiyoke Sky', 'Bangsean', 'Blu Monkey', 'Blue Carina', 'Centara Chiang Mai', 'Citadines Grand Central',
                  'Glory Boutique', 'Hotel Fuse Rayong', 'Karin', 'Le cassia', 'Lit Bangkok', 'Madera Residence', 'Nadee 10', 'Novotel Rayong Star Centre', 
                  'Oakwood', 'Phavina Hotel Rayong', 'Romantic', 'Seabed Grand', 'Sirin', 'Star Convention', 'The Blanket', 'The Opium',
                  'The Quartier', 'Taxi Company', 'Taxi Siam inter Company', 'Taxi bangkok', 'กรุงเทพ']
    
    list_folder = [IMAGE_FOLDER_HOTEL, IMAGE_FOLDER_TAXI, AMORA_THAPAE, BAIYOKE_SKY, BANGSEAN, BLU_MONKEY, BLUE_CARINA, CENTARA_CHIANG_MAI, CITADINES_GRAND_CENTRAL, 
                   GLORY_BOUTIQUE, HOTEL_FUSE_RAYONG, KARIN, LE_CASSIA, LIT_BANGKOK, MADERA_RESIDENCE, NADEE_10, NOVOTEL_RAYONG_STAR_CENTRE, OAKWOOD,
                   PHAVINA_HOTEL_RAYONG, ROMANTIC, SEABED_GRAND, SIRIN, STAR_CONVENTION, THE_BLANKET, THE_OPIUM, THE_QUARTIER, TAXI_COMPANY, TAXI_SIAM_INTER_COMPANY,
                   TAXI_BANGKOK, IMAGE_FOLDER_HOTEL_BANGKOK, IMAGE_FOLDER_HOTEL_CHIANG_MAI, IMAGE_FOLDER_HOTEL_CHONBURI, IMAGE_FOLDER_HOTEL_PHUKET, IMAGE_FOLDER_HOTEL_KHON_KAEN,
                   IMAGE_FOLDER_HOTEL_RAYONG]
    folder = str(folder)

    for i in range(len(list_folder)):
        if folder == list_input[i]:
            return send_from_directory(list_folder[i], image_name)

    return print("Invalid folder")

#--------------------MainPage----------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hotel', methods=['GET', 'POST'])
def Hotelpage():
    if request.method == 'POST':
        location_list_thai = ['กรุงเทพ', 'เชียงใหม่', 'ชลบุรี', 'ภูเก็ต', 'ขอนแก่น', 'ระยอง']
        location_list_eng = ['Bangkok', 'Chiang mai', 'Chonburi', 'Phuket', 'Khon kaen', 'Rayong']
        all_loca_list = [location_list_thai, location_list_eng]
        folder_list = [IMAGE_FOLDER_HOTEL_BANGKOK, IMAGE_FOLDER_HOTEL_CHIANG_MAI, IMAGE_FOLDER_HOTEL_CHONBURI,
                       IMAGE_FOLDER_HOTEL_PHUKET,  IMAGE_FOLDER_HOTEL_KHON_KAEN, IMAGE_FOLDER_HOTEL_RAYONG]

        location = request.form['Location']
        location = location.lower()


        if location == '':
            hotel_list = control.get_hotel_list
            images = os.listdir(IMAGE_FOLDER_HOTEL)
            return render_template('hotel.html', hotels=hotel_list, images=images, location="in Thailand")
        elif location != '':
            for location_list in all_loca_list:
                for i in range(len(location_list)):
                    if location.lower() == location_list[i].lower():
                        hotel_list = control.seach_hotel_from_location(location_list_thai[i])
                        images = os.listdir(folder_list[i])
                        locate = location_list_eng[i]
                        return render_template('hotel.html', hotels=hotel_list, images=images, location=f'in {locate}')
            return render_template('hotel.html', hotels=[], images=[], location="Not Found")
    else:  
        hotel_list = control.get_hotel_list
        images = os.listdir(IMAGE_FOLDER_HOTEL)
        return render_template('hotel.html', hotels=hotel_list, images=images, location="in Thailand")
            
@app.route('/taxi')
def Taxipage():
    images = os.listdir(IMAGE_FOLDER_TAXI)
    return render_template('taxi.html', taxis=taxi_list, images=images)

@app.route('/report')
def Reportpage():
    return render_template('report.html')

@app.route('/about')
def Aboutpage():
    return render_template('about.html')

@app.route('/contract')
def Contract():
    return render_template('contract.html')

@app.route('/feedback')
def Feedback():
    return render_template('feedback.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        account = control.seach_account(session['username'])
        transection = account.get_transaction
        return render_template('profile.html', transection=transection, account=account)
    else:
        return render_template('index.html')


#--------------------Login-----Logout-----Register------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if 'username' in session:  # เช็คว่ามี session ของ username หรือไม่
        return redirect(url_for('index'))  # ถ้ามีให้ redirect ไปที่หน้า index
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for account in account_list:
            if username == account.get_name and password == account.get_password:
                session['username'] = username
                if 'next' in session:
                    if session['next'] == 'http://127.0.0.1:5000/register':
                        return render_template('index.html')
                    return redirect(session['next'])
                else:
                    return redirect(url_for('index'))
            elif username == '' and password == '':
                return render_template('login.html', popup=True , warning="Please enter your Username and Password.")
            elif username == '':
                return render_template('login.html', popup=True , warning="Please enter your Username.")
            elif password == '':
                return render_template('login.html', popup=True , warning="Please enter your Password.")
            
    session['next'] = request.referrer
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['next'] = request.referrer
    session.pop('username', None)
    return redirect(session['next'] if 'next' in session else url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mail = request.form['mail']
        phone = request.form['phone']
        for account in account_list:
            if username == '' and password == '' and mail == '' and phone == '':
                return render_template('register.html', popup=True, warning="Please enter your information.")
            elif username == '':
                return render_template('register.html', popup=True, warning="Please enter your Username.")
            elif password == '':
                return render_template('register.html', popup=True, warning="Please enter your Password.")
            elif mail == '':
                return render_template('register.html', popup=True, warning="Please enter your Mail.")
            elif phone == '':
                return render_template('register.html', popup=True, warning="Please enter your Phone.")
            elif username == account.get_name:
                return render_template('register.html', popup=True, warning="This Username already in use.")
            elif 'admin' in username:
                return render_template('register.html', popup=True, warning="This Username can't use.")
            elif len(username) < 4:
                return render_template('register.html', popup=True, warning="Your Username too short.")
            elif len(password) < 4:
                return render_template('register.html', popup=True, warning="Your Password too short.")
            else:
                creat_account(username, password, mail) 
                return redirect(url_for('login'))  
    return render_template('register.html')

#--------------------------Hotel-----------------------------------------------------------

@app.route('/hotel/<hotel_name>')
def hotel_page(hotel_name):
    folder_name = globals()[hotel_name.upper().replace(" ", "_")]
    images = os.listdir(folder_name)
    hotel = control.seach_hotel_from_name(hotel_name)
    room_list = hotel.search_available_room
    return render_template(f'{hotel_name}.html', rooms=room_list, images=images, hotels=hotel)

#--------------------------Taxi-----------------------------------------------------------

@app.route('/taxi/<taxi_name>')
def taxi_page(taxi_name):
    folder_name = globals()[taxi_name.upper().replace(" ", "_")]
    images = os.listdir(folder_name)
    taxi = control.seach_taxi(taxi_name)
    car = taxi.seach_available_car
    return render_template(f'{taxi_name}.html', cars=car, images=images, taxis=taxi)

#--------------------------Test-----------------------------------------------------------

@app.route('/pay')
def pay():
    type = request.args.get('type')
    hotel = request.args.get('hotel')
    room = request.args.get('room')
    taxi = request.args.get('taxi')
    car = request.args.get('car')

    if session.get('username') is None:
        return redirect(url_for('login'))
    elif type == 'hotel':
        hotels = control.seach_hotel_from_name(hotel)
        rooms = hotels.search_room(int(room))
        return render_template('pay.html', hotel=hotels, room=rooms, type=type)
    elif type == 'taxi':
        taxis = control.seach_taxi(taxi)
        cars = taxis.search_car_from_phone(car)
        return render_template('pay.html', car=cars, taxi=taxis, type=type)

        

@app.route('/confirm_page', methods=['GET', 'POST'])
def confirm_page():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            type = request.form.get('type')
            if type == 'hotel':
                hotel_name = request.form.get('hotel_name')
                room_number = request.form.get('room_number')
                date_in = request.form.get('date_in')
                date_out = request.form.get('date_out')
                head_count_hotel = request.form.get('head_count')

                hotel = control.seach_hotel_from_name(hotel_name)
                room = hotel.search_room(int(room_number))

                date1 = int(date_in[8:])
                date2 = int(date_out[8:])
                month1 = int(date_in[5:7])
                month2 = int(date_out[5:7])
                year1 = int(date_in[0:4])
                year2 = int(date_out[0:4])

                day = date2 - date1
                month = month2 - month1
                year = year2 - year1
                price_room = room.get_price
                day_count = 0
                if year > 0:
                    if month > 0:
                        price = (day + (month *30) + (year *365)) * price_room
                        day_count += (day + (month *30) + (year *365))
                    else:
                        price = (day + (year *365)) * price_room
                        day_count += (day + (year *365))
                else:
                    if month > 0:
                        price = (day + (month *30)) * price_room
                        day_count += (day + (month *30))
                    else:
                        price = day * price_room
                        day_count += day
                

                return render_template('confirm.html', hotel=hotel, room=room, date_in=date_in, date_out=date_out, head_count=head_count_hotel, day=day_count , price=price, type='hotel')
            elif type == 'taxi':
                taxi_name = request.form.get('taxi_name')
                car_phone = request.form.get('car_phone')
                date = request.form.get('date_in')
                head_count_taxi = request.form.get('head_count')
                source = request.form.get('source')
                des = request.form.get('des')
                travel_type = request.form.get('travel_type')

                taxi = control.seach_taxi(taxi_name)
                car = taxi.search_car_from_phone(car_phone)
                price = car.get_price

                if travel_type == 'เที่ยวเดียว':
                    return render_template('confirm.html', taxi=taxi, car=car, date=date, head_count=head_count_taxi, source=source, des=des, price=price, travel_type=travel_type, type='taxi')
                elif travel_type == 'ไป-กลับ':
                    price *= 2
                    return render_template('confirm.html', taxi=taxi, car=car, date=date, head_count=head_count_taxi, source=source, des=des, price=price, travel_type=travel_type, type='taxi')

    return redirect(url_for('index'))
        

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            type = request.form.get('type')
            if type == 'hotel':
                hotel_name = request.form.get('hotel_name')
                room_type = request.form.get('room_type')
                room_number = request.form.get('room_number')
                head_count = request.form.get('head_count')
                date_in = request.form.get('date_in')
                date_out = request.form.get('date_out')
                price = request.form.get('price')

                hotel = control.seach_hotel_from_name(hotel_name)
                room = hotel.search_room(int(room_number))
                room.set_date_in(date_in)
                room.set_date_out(date_out)

                account = control.seach_account(session['username'])
                admin = control.seach_account('admin')
                if session['username'] == 'admin':
                    account.add_transaction(Transection_hotel(hotel_name, room_type, date_in, date_out, price,head_count, session['username']))
                else:
                    admin.add_transaction(Transection_hotel(hotel_name, room_type, date_in, date_out, price,head_count, session['username']))
                    account.add_transaction(Transection_hotel(hotel_name, room_type, date_in, date_out, price,head_count, session['username']))
                return render_template('index.html')
            
            elif type == 'taxi':
                taxi_name = request.form.get('taxi_name')
                car_type = request.form.get('car_type')
                car_phone = request.form.get('car_phone')
                head_count = request.form.get('head_count')
                date = request.form.get('date')
                travel_type = request.form.get('travel_type')
                source = request.form.get('source')
                des = request.form.get('des')
                price = request.form.get('price')

                taxi = control.seach_taxi(taxi_name)
                car = taxi.search_car_from_phone(car_phone)
                car.set_travel_type(travel_type)
                car.set_travel_date(date)
                car.set_pickup_location(source)
                car.set_destination_location(des)

                account = control.seach_account(session['username'])
                admin = control.seach_account('admin')
                if session['username'] == 'admin':
                    account.add_transaction(Transection_taxi(taxi_name, car_type, date, travel_type, source, des, price, head_count, session['username']))
                else:
                    account.add_transaction(Transection_taxi(taxi_name, car_type, date, travel_type, source, des, price, head_count, session['username']))
                    admin.add_transaction(Transection_taxi(taxi_name, car_type, date, travel_type, source, des, price, head_count, session['username']))
                return render_template('index.html')

    
#----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)



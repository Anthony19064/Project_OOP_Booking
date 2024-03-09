from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from instance import *
import os


creat_instance()
app = Flask(__name__)
app.secret_key = 'booking'
hotel_list = control.get_hotel_list
hotel_list.sort(key=lambda x: x._Hotel__name)
taxi_list = control.get_taxi_list
taxi_list.sort(key=lambda x: x._Taxi__name)



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
        adult = request.form['Adult']
        date = request.form['date']

        if location == '':
            hotel_list = control.get_hotel_list
            hotel_list.sort(key=lambda x: x._Hotel__name)
            images = os.listdir(IMAGE_FOLDER_HOTEL)
            return render_template('hotel.html', hotels=hotel_list, images=images, location="in Thailand")
        elif location != '':
            for location_list in all_loca_list:
                for i in range(len(location_list)):
                    if location.lower() == location_list[i].lower():
                        hotel_list = control.seach_hotel_from_location(location_list_thai[i])
                        hotel_list.sort(key=lambda x: x._Hotel__name)
                        images = os.listdir(folder_list[i])
                        locate = location_list_eng[i]
                        return render_template('hotel.html', hotels=hotel_list, images=images, location=f'in {locate}')
            return render_template('hotel.html', hotels=[], images=[], location="Not Found")

    else:  
        hotel_list = control.get_hotel_list
        hotel_list.sort(key=lambda x: x._Hotel__name)
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

#--------------------Login-----Logout-----Register------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    account_list = control.get_account_list
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
            elif username == '':
                return render_template('login.html', popup=True , warning="Please enter your Password.")
            elif username == account.get_name and password != account.get_password:
                return render_template('login.html', popup=True , warning="Password wrong  Pleas try agin.")
            elif username != account.get_name and password == account.get_password:
                return render_template('login.html', popup=True , warning="Username wrong  Pleas try agin.")
            else:
                return render_template('login.html', popup=True , warning="We couldn't find your account in the system. Please try again.")
    session['next'] = request.referrer
    return render_template('login.html')



@app.route('/logout')
def logout():
    session['next'] = request.referrer
    session.pop('username', None)
    return redirect(session['next'] if 'next' in session else url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    account_list = control.get_account_list
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mail = request.form['mail']
        phone = request.form['phone']
        print(username)
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

@app.route('/testdata')
def test_get_data():
    hotel = request.args.get('hotel')
    room = request.args.get('room')
    hotels = control.seach_hotel_from_name(hotel)
    rooms = hotels.search_room(int(room))
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        return render_template('testdata.html', hotel=hotels, room=rooms)
    

#----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)



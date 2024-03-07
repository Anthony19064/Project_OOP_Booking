from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from instance import *
import os


creat_instance()

app = Flask(__name__)
app.secret_key = 'booking'  
hotel_list = control.get_hotel_list
hotel_list.sort(key=lambda x: x._Hotel__name)
taxi_list = control.get_taxi_list
account_list = control.get_account_list


# กำหนดเส้นทางสำหรับโฟลเดอร์รูปภาพ
IMAGE_FOLDER_HOTEL = 'hotel'
IMAGE_FOLDER_TAXI = 'taxi'
AMORA_THAPAE = 'room_amorathapae'
BAIYOKE_SKY_HOTEL = 'room_baiyokeskyhotel'
BANGSEAN_HOTEL = 'room_bangseanhotel'
BLU_MONKEY_HOTEL = 'room_blumonkeyhotel'
BLUE_CARINA_HOTEL = 'room_blumonkeyhotel'
CENTARA_CHIANG_MAI = 'room_centarachiangmai'
CITADINES_GRAND_CENTRAL = 'room_citadinesgrandcentral'
GLORY_BOUTIQUE_HOTEL = 'room_gloryboutique'
HOTEL_FUSE_RAYONG = 'room_hotelfuserayong'
KARIN_HOTEL = 'room_karinhotel'
LE_CASSIA_HOTEL = 'room_lecassiahotel'
LIT_BANGKOK = 'room_litbangkok'
MADERA_RESIDENCE = 'room_maderaresidence'
NADEE_10_HOTEL = 'room_nadee10hotel'
NOVOTEL_RAYONG_STAR_CENTRE = 'room_novotelrayongstarcentre'
OAKWOOD_HOTEL = 'room_oakwoodhotel'
PHAVINA_HOTEL_RAYONG = 'room_phavinahotelrayong'
ROMANTIC_HOTEL = 'room_romantichotel'
SEABED_GRAND_HOTEL = 'room_seabedgrandhotel'
SIRIN_HOTEL = 'room_sirinhotel'
STAR_CONVENTION_HOTEL = 'room_starconventionhotel'
THE_BLANKET_HOTEL = 'room_theblankethotel'
THE_OPIUM = 'room_theopium'
THE_QUEARTIER_HOTEL = 'room_thequeartierhotel'


@app.route('/images/<path:folder>/<path:image_name>')
def get_image(folder, image_name):
    folder = str(folder)
    if folder == "hotel":
        return send_from_directory(IMAGE_FOLDER_HOTEL, image_name)
    elif folder == "taxi":
        return send_from_directory(IMAGE_FOLDER_TAXI, image_name)
    elif folder == 'Amora Thapae':
        return send_from_directory(AMORA_THAPAE, image_name)
    elif folder == 'Baiyoke Sky Hotel':
        return send_from_directory(BAIYOKE_SKY_HOTEL, image_name)
    elif folder == 'Bangsean Hotel':
        return send_from_directory(BANGSEAN_HOTEL, image_name)
    elif folder == 'Blu Monkey Hotel':
        return send_from_directory(BLU_MONKEY_HOTEL, image_name)
    elif folder == 'Blue Carina Hotel':
        return send_from_directory(BLUE_CARINA_HOTEL, image_name)
    elif folder == 'Centara Chiang Mai':
        return send_from_directory(CENTARA_CHIANG_MAI, image_name)
    elif folder == 'Citadines Grand Central':
        return send_from_directory(CITADINES_GRAND_CENTRAL, image_name)
    elif folder == 'Glory Boutique':
        return send_from_directory(GLORY_BOUTIQUE_HOTEL, image_name)
    elif folder == 'Hotel Fuse Rayong':
        return send_from_directory(HOTEL_FUSE_RAYONG, image_name)
    elif folder == 'Karin Hotel':
        return send_from_directory(KARIN_HOTEL, image_name)
    elif folder == 'Le cassia Hotel':
        return send_from_directory(LE_CASSIA_HOTEL, image_name)
    elif folder == 'Lit Bangkok':
        return send_from_directory(LIT_BANGKOK, image_name)
    elif folder == 'Madera Residence':
        return send_from_directory(MADERA_RESIDENCE, image_name)
    elif folder == 'Nadee 10 Hotel':
        return send_from_directory(NADEE_10_HOTEL, image_name)
    elif folder == 'Novotel Rayong Star Centre':
        return send_from_directory(NOVOTEL_RAYONG_STAR_CENTRE, image_name)
    elif folder == 'Oakwood Hotel':
        return send_from_directory(OAKWOOD_HOTEL, image_name)
    elif folder == 'Phavina Hotel Rayong':
        return send_from_directory(PHAVINA_HOTEL_RAYONG, image_name)
    elif folder == 'Romantic Hotel':
        return send_from_directory(ROMANTIC_HOTEL, image_name)
    elif folder == 'Seabed Grand Hotel':
        return send_from_directory(SEABED_GRAND_HOTEL, image_name)
    elif folder == 'Sirin Hotel':
        return send_from_directory(SIRIN_HOTEL, image_name)
    elif folder == 'Star Convention Hotel':
        return send_from_directory(STAR_CONVENTION_HOTEL, image_name)
    elif folder == 'The Blanket Hotel':
        return send_from_directory(THE_BLANKET_HOTEL, image_name)
    elif folder == 'The Opium':
        return send_from_directory(THE_OPIUM, image_name)
    elif folder == 'The Quartier Hotel':
        return send_from_directory(THE_QUEARTIER_HOTEL, image_name)
    
    
    else:
        return print("Invalid folder")
print('Please')
#--------------------MainPage----------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hotel')
def Hotelpage():
    images = os.listdir(IMAGE_FOLDER_HOTEL)
    return render_template('hotel.html',hotels=hotel_list, images=images)

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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for account in account_list:
            if username == account.get_name and password == account.get_password:
                session['username'] = username
                return redirect(url_for('index'))
        return render_template('login.html') 
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for account in account_list:
            if username == account.get_name:
                return 'Username already exists!'
            else:
                creat_account(username, password) 
                return redirect(url_for('login'))  
    return render_template('register.html')



#--------------------------Hotel-----------------------------------------------------------

@app.route('/<hotel_name>')
def hotel_page(hotel_name):
    folder_name = globals()[hotel_name.upper().replace(" ", "_")]
    images = os.listdir(folder_name)
    hotel = control.seach_hotel_from_name(hotel_name)
    room_list = hotel.get_room_list
    return render_template(f'{hotel_name}.html', rooms=room_list, images=images, hotels=hotel)




# @app.route('/Amora Thapae')
# def AmoraThapae():
#     images = os.listdir(IMAGE_FOLDER_ROOM)
#     hotel = control.seach_hotel_from_name('Amora Thapae')
#     room_list = hotel.get_room_list
#     return render_template('Amora Thapae.html',rooms=room_list, images=images)

# @app.route('/Baiyoke Sky Hotel')
# def BaiyokeSkyHotel():
#     images = os.listdir(IMAGE_FOLDER_ROOM)
#     hotel = control.seach_hotel_from_name('Baiyoke Sky Hotel')
#     room_list = hotel.get_room_list
#     return render_template('Baiyoke Sky Hotel.html',rooms=room_list, images=images)

# @app.route('/Novotel Rayong Star Centre')
# def NovotelRayongStarCentre():
#     return render_template('Novotel Rayong Star Centre.html')

# @app.route('/Hotel Fuse Rayong')
# def HotelFuseRayong():
#     return render_template('Hotel Fuse Rayong.html')

# @app.route('/Phavina Hotel Rayong')
# def PhavinaHotelRayong():
#     return render_template('Phavina Hotel Rayong.html')

# @app.route('/Star Convention Hotel')
# def StarConventionHotel():
#     return render_template('Star Convention Hotel.html')

# @app.route('/The Blanket Hotel')
# def TheBlanketHotel():
#     return render_template('The Blanket Hotel.html')

# @app.route('/Seabed Grand Hotel')
# def SeabedGrandHotel():
#     return render_template('Seabed Grand Hotel.html')

# @app.route('/Blu Monkey Hotel')
# def BluetoothMonkeyHotel():
#     return render_template('Blu Monkey Hotel.html')

# @app.route('/Blue Carina Hotel')
# def BlueCarinaHotel():
#     return render_template('Blue Carina Hotel.html')

# @app.route('/Le cassia Hotel')
# def LecassiaHotel():
#     return render_template('Le cassia Hotel.html')

# @app.route('/Romantic Hotel')
# def RomanticHotel():
#     return render_template('Romantic Hotel.html')

# @app.route('/Sirin Hotel')
# def TherinHotel():
#     return render_template('Sirin Hotel.html')

# @app.route('/Nadee 10 Hotel')
# def Nadee10Hotel():
#     return render_template('Nadee 10 Hotel.html')

# @app.route('/Madera Residence')
# def MaderaResidence():
#     return render_template('Madera Residence.html')

# @app.route('/Karin Hotel')
# def KarinHotel():
#     return render_template('Karin Hotel.html')

# @app.route('/Citadines Grand Central')
# def GrandCentral():
#     return render_template('Citadines Grand Central.html')

# @app.route('/The Quartier Hotel')
# def QuartierHotel():
#     return render_template('The Quartier Hotel.html')

# @app.route('/Oakwood Hotel')
# def OakwoodHotel():
#     return render_template('Oakwood Hotel.html')

# @app.route('/The Opium')
# def TheOpium():
#     return render_template('The Opium.html')

# @app.route('/Glory Boutique')
# def GloryBoutique():
#     return render_template('Glory Boutique.html')

# @app.route('/Bangsean Hotel')
# def BangseanHotel():
#     return render_template('Bangsean Hotel.html')

# @app.route('/Centara Chiang Mai')
# def CentaraChiangMai():
#     return render_template('Centara Chiang Mai.html')

# @app.route('/Lit Bangkok')
# def LitBangkok():
#     return render_template('Lit Bangkok.html')

if __name__ == "__main__":
    app.run(debug=True)

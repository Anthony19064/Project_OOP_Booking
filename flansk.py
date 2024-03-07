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


@app.route('/images/<path:folder>/<path:image_name>')
def get_image(folder, image_name):
    list_input = ["hotel", "taxi", 'Amora Thapae','Baiyoke Sky', 'Bangsean', 'Blu Monkey', 'Blue Carina', 'Centara Chiang Mai', 'Citadines Grand Central',
                  'Glory Boutique', 'Hotel Fuse Rayong', 'Karin', 'Le cassia', 'Lit Bangkok', 'Madera Residence', 'Nadee 10', 'Novotel Rayong Star Centre', 
                  'Oakwood', 'Phavina Hotel Rayong', 'Romantic', 'Seabed Grand', 'Sirin', 'Star Convention', 'The Blanket', 'The Opium',
                  'The Quartier']
    list_folder = [IMAGE_FOLDER_HOTEL, IMAGE_FOLDER_TAXI, AMORA_THAPAE, BAIYOKE_SKY, BANGSEAN, BLU_MONKEY, BLUE_CARINA, CENTARA_CHIANG_MAI, CITADINES_GRAND_CENTRAL, 
                   GLORY_BOUTIQUE, HOTEL_FUSE_RAYONG, KARIN, LE_CASSIA, LIT_BANGKOK, MADERA_RESIDENCE, NADEE_10, NOVOTEL_RAYONG_STAR_CENTRE, OAKWOOD,
                   PHAVINA_HOTEL_RAYONG, ROMANTIC, SEABED_GRAND, SIRIN, STAR_CONVENTION, THE_BLANKET, THE_OPIUM, THE_QUARTIER]
    folder = str(folder)

    for i in range(len(list_folder)):

        if folder == list_input[i]:
            return send_from_directory(list_folder[i], image_name)

    return print("Invalid folder")

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

@app.route('/testdata')
def test_get_data():
    hotel = request.args.get('hotel')
    room = request.args.get('room')
    hotel = control.seach_hotel_from_name(hotel)
    return render_template('testdata.html', hotel=hotel, room=room)

#----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)



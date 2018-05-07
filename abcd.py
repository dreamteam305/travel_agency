from flask import *
from flaskext.mysql import MySQL

app = Flask(__name__)


mysql = MySQL()



# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bogdan322464'
app.config['MYSQL_DATABASE_DB'] = 'travel_agency'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

@app.route('/hotel.html')
def hotel():
   accomodation_names = mysql.connect().cursor()
   accomodation_names.execute("SELECT distinct Accomodation_Name FROM `travel_agency`.`Accomodation`;")
   # flight_carr= flight_carrier.fetchall()

   accomodation_type = mysql.connect().cursor()
   accomodation_type.execute("SELECT distinct Accomodation_Type FROM `travel_agency`.`Accomodation`;")

   rate_per_night = mysql.connect().cursor()
   rate_per_night.execute("SELECT distinct Rate_Per_Night FROM `travel_agency`.`Accomodation`;")



   # "Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID "

   return render_template("hotel.html", AccoName=accomodation_names.fetchall(), AccoType=accomodation_type.fetchall(),
                          AccoRate = rate_per_night.fetchall())

@app.route('/car.html')
def car():
   car_company = mysql.connect().cursor()
   car_company.execute("SELECT distinct Company FROM `travel_agency`.`Car`;")
   # flight_carr= flight_carrier.fetchall()

   car_city = mysql.connect().cursor()
   car_city.execute("SELECT distinct Park_Addr FROM `travel_agency`.`Car`;")

   car_type = mysql.connect().cursor()
   car_type.execute("SELECT distinct Car_Type FROM `travel_agency`.`Car`;")




   return render_template("car.html", CarComp = car_company.fetchall(), CarCity = car_city.fetchall(),
                          CarType = car_type.fetchall())

@app.route('/a')
def a():
   return "<form action=>"

#main path
@app.route('/')
def main():
   flight_carrier = mysql.connect().cursor()
   flight_carrier.execute("SELECT distinct Flight_Carrier FROM `travel_agency`.`flight`;")
   # flight_carr= flight_carrier.fetchall()

   flight_source = mysql.connect().cursor()
   flight_source.execute("SELECT distinct Source_Airport_ID FROM `travel_agency`.`flight`;")

   flight_destination = mysql.connect().cursor()
   flight_destination.execute("SELECT distinct Destination_Airport_ID FROM `travel_agency`.`flight`;")

   flight_clas = mysql.connect().cursor()
   flight_clas.execute("SELECT distinct Flight_Class FROM `travel_agency`.`flight`;")

   # "Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID "

   return render_template("index.html", flight_carr=flight_carrier.fetchall(), flight_src=flight_source.fetchall(),
                          flight_dest=flight_destination.fetchall(), flight_c=flight_clas.fetchall())

@app.route('/index.html')
def index():
   flight_carrier = mysql.connect().cursor()
   flight_carrier.execute("SELECT distinct Flight_Carrier FROM `travel_agency`.`flight`;")
   # flight_carr= flight_carrier.fetchall()

   flight_source = mysql.connect().cursor()
   flight_source.execute("SELECT distinct Source_Airport_ID FROM `travel_agency`.`flight`;")

   flight_destination = mysql.connect().cursor()
   flight_destination.execute("SELECT distinct Destination_Airport_ID FROM `travel_agency`.`flight`;")

   flight_clas = mysql.connect().cursor()
   flight_clas.execute("SELECT distinct Flight_Class FROM `travel_agency`.`flight`;")

   # "Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID "

   return render_template("index.html", flight_carr=flight_carrier.fetchall(), flight_src=flight_source.fetchall(),
                          flight_dest=flight_destination.fetchall(), flight_c=flight_clas.fetchall())



@app.route('/flight.html')
def flight():
   # cursor = mysql.connect().cursor()
   # cursor.execute("SELECT * FROM Employee")
   #Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID
   flight_carrier = mysql.connect().cursor()
   flight_carrier.execute("SELECT distinct Flight_Carrier FROM `travel_agency`.`flight`;")
   # flight_carr= flight_carrier.fetchall()

   flight_source = mysql.connect().cursor()
   flight_source.execute("SELECT distinct Source_Airport_ID FROM `travel_agency`.`flight`;")

   flight_destination = mysql.connect().cursor()
   flight_destination.execute("SELECT distinct Destination_Airport_ID FROM `travel_agency`.`flight`;")

   flight_clas = mysql.connect().cursor()
   flight_clas.execute("SELECT distinct Flight_Class FROM `travel_agency`.`flight`;")



                          # "Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID "

   return render_template('flight.html', flight_carr=flight_carrier.fetchall(), flight_src = flight_source.fetchall(), flight_dest= flight_destination.fetchall(), flight_c = flight_clas.fetchall())


@app.route("/<filename>.html")
def htmlRoute(filename):
   return render_template(filename+".html")






if __name__ == "__main__":
   app.run(debug= True)


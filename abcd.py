from flask import *
from flaskext.mysql import MySQL

app = Flask(__name__)


mysql = MySQL()

dict = {}


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

   accomodation_type = mysql.connect().cursor()
   accomodation_type.execute("SELECT distinct Accomodation_Type FROM `travel_agency`.`Accomodation`;")

   rate_per_night = mysql.connect().cursor()
   rate_per_night.execute("SELECT distinct Rate_Per_Night FROM `travel_agency`.`Accomodation`;")





   return render_template("hotel.html", AccoName=accomodation_names.fetchall(), AccoType=accomodation_type.fetchall(),
                          AccoRate = rate_per_night.fetchall())

@app.route('/car.html')
def car():
   car_company = mysql.connect().cursor()
   car_company.execute("SELECT distinct Company FROM `travel_agency`.`Car`;")

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


   flight_source = mysql.connect().cursor()
   flight_source.execute("SELECT distinct Source_Airport_ID FROM `travel_agency`.`flight`;")

   flight_destination = mysql.connect().cursor()
   flight_destination.execute("SELECT distinct Destination_Airport_ID FROM `travel_agency`.`flight`;")

   flight_clas = mysql.connect().cursor()
   flight_clas.execute("SELECT distinct Flight_Class FROM `travel_agency`.`flight`;")

   review = mysql.connect().cursor()
   review.execute("SELECT distinct Detailed_Review FROM `travel_agency`.`Review`;")

   return render_template("index.html", flight_carr=flight_carrier.fetchall(), flight_src=flight_source.fetchall(),
                          flight_dest=flight_destination.fetchall(), flight_c=flight_clas.fetchall(),
                          Rev=review.fetchall())

@app.route('/index.html')
def index():
   flight_carrier = mysql.connect().cursor()
   flight_carrier.execute("SELECT distinct Flight_Carrier FROM `travel_agency`.`flight`;")


   flight_source = mysql.connect().cursor()
   flight_source.execute("SELECT distinct Source_Airport_ID FROM `travel_agency`.`flight`;")

   flight_destination = mysql.connect().cursor()
   flight_destination.execute("SELECT distinct Destination_Airport_ID FROM `travel_agency`.`flight`;")

   flight_clas = mysql.connect().cursor()
   flight_clas.execute("SELECT distinct Flight_Class FROM `travel_agency`.`flight`;")

   review = mysql.connect().cursor()
   review.execute("SELECT distinct Detailed_Review FROM `travel_agency`.`Review`;")

   return render_template("index.html", flight_carr=flight_carrier.fetchall(), flight_src=flight_source.fetchall(),
                          flight_dest=flight_destination.fetchall(), flight_c=flight_clas.fetchall(),
                            Rev = review.fetchall())



@app.route('/flight.html')
def flight():

   flight_carrier = mysql.connect().cursor()
   flight_carrier.execute("SELECT distinct Flight_Carrier FROM `travel_agency`.`flight`;")


   flight_source = mysql.connect().cursor()
   flight_source.execute("SELECT distinct Source_Airport_ID FROM `travel_agency`.`flight`;")

   flight_destination = mysql.connect().cursor()
   flight_destination.execute("SELECT distinct Destination_Airport_ID FROM `travel_agency`.`flight`;")

   flight_clas = mysql.connect().cursor()
   flight_clas.execute("SELECT distinct Flight_Class FROM `travel_agency`.`flight`;")

   return render_template('flight.html', flight_carr=flight_carrier.fetchall(), flight_src = flight_source.fetchall(), flight_dest= flight_destination.fetchall(), flight_c = flight_clas.fetchall())

@app.route('/bus.html')
def bus():
   # # cursor = mysql.connect().cursor()
   # # cursor.execute("SELECT * FROM Employee")
   # #Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID
   # bus_company = mysql.connect().cursor()
   # bus_company.execute("SELECT distinct Bus_Company FROM `travel_agency`.`Bus`;")
   # # flight_carr= flight_carrier.fetchall()
   #
   # bus_source = mysql.connect().cursor()
   # bus_source.execute("SELECT distinct Source_Bus_Stop FROM `travel_agency`.`Bus`;")
   #
   # bus_destination = mysql.connect().cursor()
   # bus_destination.execute("SELECT distinct Destination_Bus_Stop FROM `travel_agency`.`Bus`;")
   #
   # return render_template('bus.html', flight_carr = bus_company.fetchall(), flight_src = bus_source.fetchall(), flight_dest = bus_destination.fetchall(), flight_c=bus_destination.fetchall() )
   bus_company = mysql.connect().cursor()
   bus_company.execute("SELECT distinct Bus_Company FROM `travel_agency`.`Bus`;")

   bus_source = mysql.connect().cursor()
   bus_source.execute("SELECT distinct Source_Bus_Stop FROM `travel_agency`.`Bus`;")

   bus_destination = mysql.connect().cursor()
   bus_destination.execute("SELECT distinct Destination_Bus_Stop FROM `travel_agency`.`Bus`;")

   return render_template('bus.html', BusCom =bus_company.fetchall(), BusSrc = bus_source.fetchall(),
                          BusDes = bus_destination.fetchall())


@app.route('/cruise.html')
def cruise():
   # cursor = mysql.connect().cursor()
   # cursor.execute("SELECT * FROM Employee")
   #Flight_Carrier, Flight_Fare, Flight_Class, Source_Airport_ID, Destination_Airport_ID
   cruise_company = mysql.connect().cursor()
   cruise_company.execute("SELECT distinct Cruise_Company FROM `travel_agency`.`Cruise`;")
   # flight_carr= flight_carrier.fetchall()

   cruise_source = mysql.connect().cursor()
   cruise_source.execute("SELECT distinct Source_Port FROM `travel_agency`.`Cruise`;")

   cruise_destination = mysql.connect().cursor()
   cruise_destination.execute("SELECT distinct Destination_Port FROM `travel_agency`.`Cruise`;")

   cruise_class = mysql.connect().cursor()
   cruise_class.execute("SELECT distinct Cruise_Class FROM `travel_agency`.`Cruise`;")


   return render_template('cruise.html', CruiseCom=cruise_company.fetchall(), CruiseSrc = cruise_source.fetchall(), CruiseDes= cruise_destination.fetchall(), CruiseClass= cruise_class.fetchall())


@app.route("/Authenticate")
def Authenticate():
    id = request.args.get('Employee_ID')
    name = request.args.get('Employee_Name')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Employee where Employee_ID='" + id + "' and Employee_Name='" + name + "'")
    data = cursor.fetchone()
    if data is None:
     return "Id or Name is wrong"
    else:
     return  render_template('employee.html')

@app.route('/employee.html')
def employee():
    cur = conn.cursor()
    cur.execute("Delete From `travel_agency`.`Car` WHERE `Company` = 'favicon.ico' ")
    conn.commit()
    return render_template('employee.html')

@app.route("/<filename>.html")
def htmlRoute(filename):

   return render_template(filename+".html")

@app.route("/flightdata.html")
def flightdata():
   cur = conn.cursor()
   cur.execute("SELECT * FROM `travel_agency`.`flight`")
   data = cur.fetchall()
   return render_template('flightdata.html', data=data)

@app.route("/cardata.html")
def cardata():
   cur = conn.cursor()
   cur.execute("SELECT * FROM `travel_agency`.`Car`")
   data = cur.fetchall()
   cur.execute("Delete From `travel_agency`.`Car` WHERE `Company` = 'favicon.ico' ")
   conn.commit()
   return render_template('cardata.html', data=data)

@app.route("/busdata.html")
def busdata():
   cur = conn.cursor()
   cur.execute("SELECT * FROM `travel_agency`.`Bus`")
   data = cur.fetchall()
   return render_template('busdata.html', data=data)

@app.route("/cruisedata.html")
def cruisedata():
   cur = conn.cursor()
   cur.execute("SELECT * FROM `travel_agency`.`Cruise`")
   data = cur.fetchall()
   return render_template('cruisedata.html', data=data)

@app.route("/hoteldata.html")
def hoteldata():
   cur = conn.cursor()
   cur.execute("SELECT * FROM `travel_agency`.`Accomodation`")
   data = cur.fetchall()
   return render_template('hoteldata.html', data=data)

@app.route('/insert/<string:insert>')
def add(insert):
	cur = conn.cursor()
	cur.execute('''SELECT MAX(Car_ID) FROM `travel_agency`.`Car`''')
	maxid = cur.fetchone() #(10,)
	cur.execute('''INSERT INTO Car (Company, Park_Addr,Car_Type) 
                      VALUES (%s, 'New York', 'regular')''',  insert)
	conn.commit()
	return render_template('insertcomplete.html')

@app.route("/insert")
def addACar():
    cur = conn.cursor()
    cur.execute("Delete From `travel_agency`.`Car` WHERE `Company` = 'favicon.ico' ")
    conn.commit()
    return render_template('insert.html')

@app.route("/begin", methods =["POST"])
def tripStarter():
    dict.clear()
    dict["source"] = request.form.get("source")
    dict["destination"] = request.form.get("destination")
    dict["departure"] = request.form.get("departure")
    dict["arrival"] = request.form.get("arrival")
    dict["lux"] = request.form.get("lux")
    dict["passenger"] = request.form.get("passenger")
    print(dict)
    return redirect(url_for(request.form.get("transport")))





if __name__ == "__main__":
   app.run(debug= True)


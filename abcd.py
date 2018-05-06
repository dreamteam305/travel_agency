from flask import *
from flaskext.mysql import MySQL

app = Flask(__name__)


mysql = MySQL()



# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Jamal1994'
app.config['MYSQL_DATABASE_DB'] = 'travel_agency'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()


@app.route('/a')
def a():
   return "<form action=>"

@app.route('/')
def main():
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


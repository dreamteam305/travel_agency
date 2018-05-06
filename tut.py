from flask import*
from flaskext.mysql import MySQL

app = Flask(__name__)


#mysql = MySQL()



# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bogdan322464'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
mysql = MySQL(app)

#conn = mysql.connect()

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

@app.route("/")
def hello():
    return "Welcome to Python Flask App!"


@app.route('/getall')
def getall():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM User")
    returnvals = cursor.fetchall()
    counter = 0
    printthis = ""
    for i in returnvals:
        printthis = printthis + str(returnvals[counter]) + "\n" + str(counter)
        counter = counter + 1
    return  printthis




if __name__ == "__main__":
    app.run()
from flask import*
from flask.ext.mysql import MySQL

app = Flask(__name__)


mysql = MySQL()



# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bogdan322464'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()


@app.route('/a')
def a():
   return "<form action=>"

@app.route('/index.html')
def index():
   cursor = mysql.connect().cursor()
   cursor.execute("SELECT userName FROM User")
   return render_template('index.html', Users = cursor.fetchall())

@app.route('/')
def main():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT userName FROM User")
    return render_template('index.html', Users=cursor.fetchall())


@app.route("/<filename>.html")
def htmlRoute(filename):
   return render_template(filename+".html")






if __name__ == "__main__":
   app.run(debug= True)


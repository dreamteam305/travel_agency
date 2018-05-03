from flask import*
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def main():
   return render_template('index.html')


@app.route("/<filename>.html")
def htmlRoute(filename):
   return render_template(filename+".html")


if __name__ == "__main__":
   app.run(debug= True)


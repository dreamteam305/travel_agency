from flask import*

app = Flask(__name__)


@app.route('/')
def main():
   return render_template('index.html')


@app.route("/<filename>.html")
def htmlRoute(filename):
   return render_template(filename+".html")


if __name__ == "__main__":
   app.run(debug= True)


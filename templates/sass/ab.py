from flask import*
app = Flask(__name__, static_url_path='/sass')



@app.route("/")
def main():
    return app.send_static_file('index.html')



if __name__ == "__main__":
    app.run()
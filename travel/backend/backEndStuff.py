from bottle import *


homeDir = "C:/Users/nafi/WebStormProjects/travel_agency/"

@route('/')
def index():
    return static_file("index.html", root= homeDir+"travel/")




run(host='localhost', port=8080)
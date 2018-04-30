from bottle import*



## the absolute path to the home directory for the project
homeDir = "C:/Users/nafi/WebstormProjects/travel_agency/travel/"



### loading the index html
@route('/')
def index():
    return static_file('index.html', root=homeDir)


## loading the css file from css/path
# Static Routes
@get("css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root= homeDir+"css/")



@route("/<filepath:re:.*\.html>")
def cars(filepath):
    return static_file(filepath, root= homeDir)

@get("/images/<filepath:re:.*\.jpg>")
def img(filepath):
    return static_file(filepath, root= homeDir + "images/")

@get("js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root=homeDir+ "js/")


run(host="localhost", port= 8080, debugger= True)
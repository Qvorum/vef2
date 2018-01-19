from bottle import *

@route('/')
def index():
    return "Halló heimur nú er gaman..."

run(host='localhost', port=8080)

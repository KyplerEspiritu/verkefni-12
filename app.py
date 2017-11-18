from bottle import *

@route('/')
def index():
    return "VERKEFNI 12"

run(host='localhost', port=8080)
from bottle import *
from sys import argv

@route('/')
def index():
    return "VERKEFNI 12"

run(host='0.0.0.0', port=argv[1])
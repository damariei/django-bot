from lib.bottle import route, run

@route('/')
def index():
    return '<b>Hello World!</b>'

run(host='localhost', port=8080)

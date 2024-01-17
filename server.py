from bottle import route, run, static_file
import json

frequency_json_file = 'keystroke_frequency.json'

@route('/api/keystrokes')
def get_frequency_json_file():
    with open(frequency_json_file, 'r') as file:
        data = json.load(file)
    return data


@route('/')
@route('/index.html')
def send_index():
    return static_file('index.html', root='web/')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='web/static/')

run(host='localhost', port=8080, debug=True)
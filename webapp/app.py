from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)

default_date = '1975-01-01'
default_binary = '0000'
default_decimal = 0
default_ip = '0.0.0.0'

@app.route('/')
def index():
    templateData = {
    'date'  : default_date,
    'binary'  : default_binary,
    'decimal' : default_decimal,
    'ip': default_ip
    }
    return render_template('index.html', **templateData)

@app.route("/<date>/<binary>")
def action(date, binary):
        global default_date
        global default_binary
        global default_ip
        global default_decimal
        default_date = date
        default_binary = binary
        default_decimal = int(binary, base=2)
        default_ip = request.remote_addr
        return "OK", 200
    
@app.route("/resta")
def resta():
        number = request.args.get('number')
        value = default_decimal - int(number)
        url = 'http://' + str(default_ip) + '/' + str(value)
        x = requests.get(url)
        return x.text, 200

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

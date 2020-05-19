from flask import Flask
import serial
import time
import threading
app = Flask(__name__)

ser = serial.Serial('/dev/ttyS1', 9600)

def get_data():
    while True:
        global x 
        x = ser.readline()

thread = threading.Thread(target = get_data)
thread.start()

@app.route('/', methods=['GET','POST'])
def homePage():
    return x

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)

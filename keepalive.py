from flask import Flask
from threading import Thread
app = Flask('')

@app.route('/')
def home():
    return "Hello World!"

def run():
  app.run(host='0.0.0.0',port=8080)#127.0.0.1 or ::

def keep_alive():  
    t = Thread(target=run)
    t.start()
from flask import Flask
import os
import sys
app = Flask(__name__)

@app.route('/')
def hello_name():
   
   color = os.environ.get('choice')
   if color not in ["green","blue","black"]:
     sys.exit(1)
   else:
     return f"<h1 style='color:{color}'>Hello world</h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)
from flask import Flask,request
import os
import sys
app = Flask(__name__)
color = os.environ.get('choice')
myfile=open("testoutput","a")
myfile.write(f"choice:{color}")
@app.route('/')
def hello_name():
   myfile.write(f"input={request.args.get('input')}")
   
   if request.args.get('input') not in ["green","blue","black","red"]:
     sys.exit(1)
   else:
     return f"<h1 style='color:{color}'>Hello world with Query String {request.args.get('input')}</h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)
   myfile.close()
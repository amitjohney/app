from flask import Flask,request
import os
import sys
print(os.environ.get("ENV_NAME"))
app = Flask(__name__)
color = os.environ.get('choice')
print(os.environ.get('ENV_NAME'))
print(os.environ.get('choice'))
if os.environ.get('ENV_NAME') not in ["dev","prod"]:
  myfile=open("testoutput","a")
  myfile.write(f"Environment variable value for choice is {color}")
  myfile.close()
@app.route('/')
def hello_name():
   if os.environ.get('ENV_NAME') not in ["dev","prod"]:
     myfile=open("testoutput","a")
     myfile.write(f"input={request.args.get('input')}")
     myfile.close()
   if request.args.get('input') not in ["green","blue","black","red"]:
     
     sys.exit(1)
   else:
     return f"<h1 style='color:{color}'>Hello world with Query String {request.args.get('input')}</h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)
   
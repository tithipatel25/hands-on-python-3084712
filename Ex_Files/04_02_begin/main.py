from flask import Flask

app = Flask(__name__) #instantiate a flask object

@app.route("/") #define a route

def hello():
  return "Hello, World!"

app.run(debug=True)
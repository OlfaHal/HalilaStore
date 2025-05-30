from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Welcome to Halila Store :) This App is developed by Olfa using Python.</h1></body></html>\n"

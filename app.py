from flask import Flask

app = Flask(__name__)

@app.route("jonathan")
def index():
    return "hello world"

app.run()
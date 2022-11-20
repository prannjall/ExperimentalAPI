import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        return "Post"
    else:
        return(jsonify(hello='World'))

if __name__ == '__main__':
    app.run()

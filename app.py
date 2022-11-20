import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        if request.data:
            request_data = request.get_json()
            return jsonify(hello='World', method='POST', payload=request_data)
        else:
            return jsonify(hello='World', method='POST')
    else:
        return jsonify(hello='World', method='GET')

if __name__ == '__main__':
    app.run(debug=True)

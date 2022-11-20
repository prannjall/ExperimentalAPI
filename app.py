import datetime
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python-Flask-REST-API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


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


from flask import Flask
from flask_cors import CORS
from routes.routes import router
from flask.ext.wtf import Form
from wtforms import IntegerField, SubmitField, validators, ValidationError

PORT = 5000

app = Flask(__name__)
CORS(app)

app.register_blueprint(router, url_prefix="/math")

if __name__ == '__main__':
    app.run(port=PORT)
    
class power(calc):
    A = IntegerField("Enter Number: ")
    B = IntegerField("Enter Power: ")
    submit = SubmitField("Answer")

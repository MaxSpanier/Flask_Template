from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qrjIbgNNRr04lGUdYGoN3485zbff83749#fk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import routes

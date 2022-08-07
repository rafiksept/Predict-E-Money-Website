from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.db'
db = SQLAlchemy(app)

class Pengeluaran(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    sex = db.Column(db.Enum('Laki-Laki', 'Perempuan'), nullable = False, server_default = "Laki-Laki")
    home = db.Column(db.Enum("Yes", "No"), nullable = False, server_default = "Yes")
    langganan = db.Column(db.Integer, nullable = False)
    income = db.Column(db.Integer, nullable = False)
    pengeluaran = db.Column(db.Integer, nullable = False)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

"""
* @author : Sandun Induranga
* @since : 0.1.0
"""

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://sandu:1234@localhost[:3306/POS"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.String(20), nullable=False)

    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary


@app.route('/')
def index():

    print(db.session.query(Customer))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


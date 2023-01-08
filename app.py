from flask import Flask, render_template
import mysql.connector

"""
* @author : Sandun Induranga
* @since : 0.1.0
"""

app = Flask(__name__)


cnx = mysql.connector.connect(user='sandu', password='1234', database='POS')
cursor = cnx.cursor()


@app.route('/')
def index():

    query = 'SELECT * FROM Customer'
    cursor.execute(query)
    for customerId in cursor:
        print(customerId)
    # return render_template('index.html', query)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, redirect, url_for
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

    return render_template('index.html', customers=cursor)


@app.route('/savecustomer', methods=['get', 'post'])
def savecustomer():
    id = request.form['cusId']
    name = request.form['cusName']
    address = request.form['address']
    salary = request.form['salary']

    query = 'INSERT INTO Customer VALUES (%s, %s, %s, %s)'
    values = (id, name, address, salary)
    cursor.execute(query, values)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

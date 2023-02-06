# Caretaker/landlord adds new tenant to the tenants table
import mysql.connector

from flask import request
from app import app, cnx


@app.route('/add_tenants', methods=['POST'])
def add_tenant():
    cursor = cnx.cursor()
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone number']
    query = 'INSERT INTO tenants (name, email, phone_number) VALUES (%s, %s, %d)'
    cursor.execute(query, (name, email, phone_number))
    cnx.commit()
    cursor.close()
    return 'Tenant added successfully'

from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy

# from routes import *

app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mykeja.db'

with app.app_context():
	db = SQLAlchemy(app)

# Models
class Tenant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	ID_No = db.Column(db.Integer, unique=False, nullable=False)
	phone = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Name : {self.name}, Phone: {self.phone}"

# add tenants to db
@app.route('/add_tenant', methods=["POST"])
def profile():
	name = request.form.get("name")
	ID_No = request.form.get("ID_No")
	phone = request.form.get("phone")

	# create an object of the Profile class of models
	# and store data as a row in our datatable
	if name != '' and ID_No != '' and phone is not None:
		t = Tenant(name=name, ID_No=ID_No, phone=phone)
		db.session.add(t)
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')

@app.route('/', methods=['GET'])
def all_tenants():
	view_tenants = Tenant.query.all()
	return render_template('home.html', tenants=view_tenants)

@app.route('/delete/<int:id>')
def delete(id):
	data = Tenant.query.get(id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_tenant')
def add_tenant():
    return render_template('add_tenant.html')

@app.route('/delete/<int:id>')
def delete_tenant(id):
    return 'Delete Tenant'


if __name__ == "__main__":
    app.run(debug=True)
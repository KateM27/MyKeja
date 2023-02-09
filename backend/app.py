from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mykeja.db'

with app.app_context():
	db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Models
class Tenant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	email = db.Column(db.String(64), unique=False, nullable=False)
	phone = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Name : {self.name}, Phone: {self.phone}"

@app.route('/')
def home():
    tenants = Tenant.query.all()
    return render_template('home.html', tenants=tenants)

@app.route('/add_tenant')
def new_tenant():
    return render_template('add_tenant.html')

# add tenants to db
@app.route('/add', methods=["POST"])
def profile():
	name = request.form.get("name")
	email = request.form.get("email")
	phone = request.form.get("phone")

	# create an object of the Profile class of models
	# and store data as a row in our datatable
	if name != '' and email != '' and phone is not None:
		t = Tenant(name=name, email=email, phone=phone)
		db.session.add(t)
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
	data = Tenant.query.get(id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
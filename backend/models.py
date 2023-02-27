from app import db

class Tenant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	ID_No = db.Column(db.Integer, unique=False, nullable=False)
	phone = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Name : {self.name}, Phone: {self.phone}"
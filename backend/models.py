# from app import db
# from flask_sqlalchemy import SQLAlchemy
# from app import app

# class Tenant(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(20), unique=False, nullable=False)
# 	email = db.Column(db.String(64), unique=False, nullable=False)
# 	phone = db.Column(db.Integer, nullable=False)

# 	def __repr__(self):
# 		return f"Name : {self.name}, Phone: {self.phone}"
    
# def add_tenant(self):
#     db.session.add(self)
#     db.session.commit()

# def delete_tenant(self):
#     db.session.delete(self)
#     db.session.commit
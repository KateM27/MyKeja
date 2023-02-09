# from flask import Flask, request, redirect
# from flask.templating import render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.debug = True

# # adding configuration for using a sqlite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# # Creating an SQLAlchemy instance
# db = SQLAlchemy(app)

# # Models
# class Tenant(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(20), unique=False, nullable=False)
# 	email = db.Column(db.String(64), unique=False, nullable=False)
# 	phone = db.Column(db.Integer, nullable=False)


# 	def __repr__(self):
# 		return f"Name : {self.name}, Phone: {self.phone}"

# if __name__ == '__main__':
# 	app.run()

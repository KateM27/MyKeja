# from frontend import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# app = create_app()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mykeja.db'

with app.app_context():
    db = SQLAlchemy(app)

# db.init_app(app)

class User(db.Model):
    email = db.Column(db.String(), primary_key=True)
    firstname = db.Column(db.String())
    surname = db.Column(db.String())
    password = db.Column(db.String())
    
    def __repr__(self):
        return f"Name : {self.first_name} {self.surname}, Email: {self.email}"

if __name__ == '__main__':
    app.run(debug=True)
 
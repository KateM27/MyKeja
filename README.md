# MyKeja
A tenant management system - unifies the landlord, caretaker, and tenant.

with app.app_context():
    db = SQLAlchemy(app)
In Python:
```
>>> from app import app, db
>>> app.app_context().push()
>>> db.create_all()
```
The above command solves the error `RuntimeError: Working outside of application context`
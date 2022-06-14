from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
#wpis do bazy danych odnośnie nowego wydatku/przychodu użytkownika
class Money(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income_or_spending = db.Column(db.String(20))
    cash_or_bank = db.Column(db.String(20))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    name = db.Column(db.String(100))
    cost = db.Column(db.Float)
    currency = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

#wpis do bazy danych odnośnie nowego użytkownika
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    money = db.relationship('Money')

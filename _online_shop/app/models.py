from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy

class Product(db.modules):
    __tablename__="products"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    prise=db.Column(db.Float, nullable=False)
    
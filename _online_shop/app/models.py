from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Product(db.Model):
    __tablename__="products"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    prise=db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    stock =db.Column(db.Integer, nullable=True, default=0)
    is_active_=db.Column(db.Boolean, nullable=True, default=True)
    category   =db.Column(db.String(50), nullable=True)
    rating =db.Column(db.Float, nullable=True, default=0)
    sale=db.Column(db.Boolean, nullable=True, default=0)
from flask import Blueprint, render_template
from .models import db, Product

bp=Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
@bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('product_list.html', products=products)
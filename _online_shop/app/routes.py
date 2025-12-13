from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product

bp=Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
@bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@bp.route('/add', methods=['Get','Post'])
def add_product():
    if request.method =='Post':
        name=request.form['name']
        prise=request.form['prise']
        product=Product(name=name, prise=float(prise))
        db.session.add(product)
        db.session.commit
        flash("Product added")
        return redirect(url_for('routes.product'))
    return render_template('product_form.html',action='Add', product=None   )
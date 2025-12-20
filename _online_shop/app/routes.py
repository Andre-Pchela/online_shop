from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product

bp=Blueprint('routes', __name__)

@bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)    
@bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('index.html', products=products)

@bp.route('/add', methods=['GET','POST'])
def add_product():
    if request.method =='POST':
        name=request.form['name']
        prise=request.form['prise']
        product=Product(name=name, prise=float(prise))
        db.session.add(product)
        db.session.commit()
        #flash("Product added")
        return redirect(url_for('routes.products'))
    return render_template('product_form.html',action='Add', product=None   )
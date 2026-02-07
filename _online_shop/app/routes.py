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
    return render_template('products.html', products=products)

@bp.route('/add', methods=['GET','POST'])
def add_product():
    if request.method =='POST':
        name=request.form['name']
        prise=request.form['prise']
        description=request.form['description']
        stock=request.form['stock']        
        is_active=request.form.get('is_active')
        category=request.form['category']  
        rating=request.form['rating']  
        sale=request.form.get('sale')  
        product=Product(name=name, prise=float(prise), description=description, stock=int(stock), is_active=bool(is_active), category=category, rating=float(rating), sale=bool(sale))
        db.session.add(product)
        db.session.commit()
        #flash("Product added")
        return redirect(url_for('routes.products'))
    return render_template('product_form.html',action='Add', product=None   )
@bp.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    ##flash('Product deleted!')
    return redirect(url_for('routes.products'))

@bp.route('/update/<int:product_id>', methods=['GET','POST'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method=="POST":
        product.name=request.form['name']
        product.prise=float(request.form['prise'])
        product.description=request.form['description']
        product.stock=request.form['stock']        
        product.is_active=bool(request.form.get('is_active'))
        product.category=request.form['category']  
        product.rating=request.form['rating']  
        product.sale=bool(request.form.get('sale'))
        db.session.commit()
        return redirect(url_for('routes.products'))
    return render_template('product_form.html',action='Update', product=product   )
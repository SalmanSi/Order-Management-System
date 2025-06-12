from flask import Blueprint,redirect,render_template


routes_bp=Blueprint('routes',__name__)

@routes_bp.route('/')
def index():
    return 'index page!'

@routes_bp.route('/orders')
def list_orders():
    pass

@routes_bp.route('/orders/<int:order_id>')
def view_order(order_id):
    pass

@routes_bp.route('/orders/add')
def add_order():
    pass
@routes_bp.route('/orders/<int:order_id>/edit')
def edit_order(order_id):
    pass

@routes_bp.route('/orders/<int:order_id>/delete')
def delete_order(order_id):
    pass






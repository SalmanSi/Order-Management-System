from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from models import db, Order, Log
from forms import OrderForm, EditOrderForm
from datetime import datetime

routes_bp = Blueprint('routes', __name__, template_folder='templates')

@routes_bp.route('/')
def index():
    return redirect(url_for('routes.list_orders'))

@routes_bp.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@routes_bp.route('/orders')
@login_required
def list_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('orders.html', orders=orders)

@routes_bp.route('/orders/add', methods=['GET', 'POST'])
@login_required
def add_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(
            order_id=form.order_id.data,
            num_items=form.num_items.data,
            delivery_date=form.delivery_date.data,
            sender_name=form.sender_name.data,
            recipient_name=form.recipient_name.data,
            recipient_address=form.recipient_address.data,
            user_id=current_user.id
        )
        db.session.add(order)
        db.session.commit()

        log = Log(
            action="Created", 
            user_id=current_user.id, 
            order_id=order.id,
            order_string_id=order.order_id
        )
        db.session.add(log)
        db.session.commit()

        flash('Order added successfully!')
        return redirect(url_for('routes.list_orders'))

    return render_template('order_form.html', form=form, action="Add")

@routes_bp.route('/orders/<int:order_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        return "Unauthorized", 403

    form = EditOrderForm(obj=order)
    if form.validate_on_submit():
        # Manually update fields except order_id
        order.num_items = form.num_items.data
        order.delivery_date = form.delivery_date.data
        order.sender_name = form.sender_name.data
        order.recipient_name = form.recipient_name.data
        order.recipient_address = form.recipient_address.data
        db.session.commit()

        log = Log(
            action="Edited", 
            user_id=current_user.id, 
            order_id=order.id,
            order_string_id=order.order_id
        )
        db.session.add(log)
        db.session.commit()

        flash('Order updated!')
        return redirect(url_for('routes.list_orders'))

    return render_template('edit_order_form.html', form=form, order=order, action="Edit")

@routes_bp.route('/orders/<int:order_id>/delete')
@login_required
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        return "Unauthorized", 403

    # Store order info before deletion
    order_string_id = order.order_id
    
    log = Log(
        action="Deleted", 
        user_id=current_user.id, 
        order_id=order.id,
        order_string_id=order_string_id
    )
    db.session.add(log)
    db.session.delete(order)
    db.session.commit()

    flash('Order deleted.')
    return redirect(url_for('routes.list_orders'))

@routes_bp.route('/orders/<int:order_id>/deliver')
@login_required
def mark_delivered(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        return "Unauthorized", 403

    order.status = "Delivered"
    db.session.commit()

    log = Log(
        action="Marked Delivered", 
        user_id=current_user.id, 
        order_id=order.id,
        order_string_id=order.order_id
    )
    db.session.add(log)
    db.session.commit()

    flash("Order marked as delivered.")
    return redirect(url_for('routes.list_orders'))

@routes_bp.route('/logs')
@login_required
def view_logs():
    logs = Log.query.order_by(Log.timestamp.desc()).all()
    logs_with_orders = []
    for log in logs:
        # Create a fake order object with just the order_id for display
        if log.order_string_id:
            fake_order = type('obj', (object,), {'order_id': log.order_string_id})
        else:
            fake_order = None
        logs_with_orders.append((log, fake_order))
    return render_template('logs.html', logs_with_orders=logs_with_orders)
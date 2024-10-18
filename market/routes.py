from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.model import Item, User
from market.forms import RegisterForm, LoginForm, purchaseForm, sellForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def home_page():
    return render_template('home.html')  # Default route is set to '/'


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = purchaseForm()  # Purchase form instance
    sell_form = sellForm()  # Sell form instance

    if request.method == "POST":
        # Process purchase form
        if purchase_form.validate_on_submit():
            purchased_item = request.form.get("purchase_item")
            p_item_obj = Item.query.filter_by(name=purchased_item).first()
            if p_item_obj and current_user.can_buy(p_item_obj):
                p_item_obj.buy(current_user)
                flash(f"You have purchased {p_item_obj.name}!", category="success")
            else:
                flash("Insufficient budget or item not found.", category="danger")

        # Process sell form
        if sell_form.validate_on_submit():
            sell_item = request.form.get('sell_item')
            s_item_obj = Item.query.filter_by(name=sell_item).first()
            if s_item_obj and current_user.can_sell(s_item_obj):
                s_item_obj.sell(current_user)
                flash(f"You have sold {s_item_obj.name}!", category="success")
            else:
                flash("You cannot sell this item.", category="danger")

        return redirect(url_for('market_page'))

    # Retrieve available items and owned items
    items = Item.query.filter_by(owner=None).all()  # Available items
    owned_items = Item.query.filter_by(owner=current_user.id).all()  # User's owned items

    return render_template(
        'market.html',
        items=items,
        purchase_form=purchase_form,
        owned_items=owned_items,
        sell_form=sell_form
    )


# Route for purchasing an item
@app.route('/purchase_item/<int:item_id>', methods=['POST'])
@login_required
def purchase_item(item_id):
    item = Item.query.get_or_404(item_id)

    if current_user.can_buy(item):
        item.buy(current_user)
        flash(f"You have purchased {item.name}!", category="success")
    else:
        flash("You do not have enough budget to purchase this item.", category="danger")

    return redirect(url_for('market_page'))


# New route for selling an item
@app.route('/sell_item/<int:item_id>', methods=['POST'])
@login_required
def sell_item(item_id):
    item = Item.query.get_or_404(item_id)

    if current_user.can_sell(item):
        item.sell(current_user)
        flash(f"You have sold {item.name}!", category="success")
    else:
        flash("You cannot sell this item.", category="danger")

    return redirect(url_for('market_page'))


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email.data,
            password=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash("Account created successfully!", category="success")
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error creating the user: {err_msg}", category="danger")

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correctness(form.password.data):
            login_user(attempted_user)
            flash(f"Welcome {attempted_user.username}, you have successfully logged in!", category="success")
            return redirect(url_for('market_page'))
        else:
            flash("Invalid username or password", category="danger")

    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out successfully", category="info")
    return redirect(url_for('home_page'))  # Redirecting to home page instead of market

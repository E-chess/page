import jsonify
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user

from market import app
from market import db
from market.forms import RegisterForm, LoginForm, PurchaseItemForm
from market.models import Item, User


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/aboutus')
def about_us_page():
    return render_template('about_us.html')


@app.route("/help")
def help_page():
    flash("Drogi użtykowniku nie obsługujemy ziemniaków!", category='danger')
    return render_template('help.html')


@app.route('/tournament', methods=['GET', 'POST'])
@login_required
def tournament_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        # Purchase Item Logic
        purchased_item = request.form.get('purchased_item')

        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                flash(
                    f"Gratulacje dołączyłeś do {p_item_object.name} za {p_item_object.price}$",
                    category='success')
                return redirect(url_for('join_page', id=p_item_object.id))
            else:
                flash(
                    f"Niestety nie masz wystarczej ileości waluty aby dołączyć do {p_item_object.name}!",
                    category='danger')

        return redirect(url_for('tournament_page'))

    if request.method == "GET":
        items = Item.query.all()
        return render_template('tournament.html',
                               items=items,
                               purchase_form=purchase_form)


@app.route('/join/<string:id>')
@login_required
def join_page(id: str):
    item = Item.query.filter_by(id=id).first()
    return render_template('tournament_join.html', id_api=item.id_api, name=item.name, price=item.price,
                           description=item.description)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              password=form.password.data,
                              email_address=form.email_address.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f"Konto utworzono pomyślnie! Zostałeś zalogowany do konta {user_to_create.username}",
            category='success')
        return redirect(url_for('tournament_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Wystąpił problem z utważeniem konta: {err_msg}',
                  category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Zostałeś pomyślnie zalogowany do konta {attempted_user.username}',
                  category='success')
            return redirect(url_for('tournament_page'))
        else:
            flash('Nazwa lub hasło użytkownika niezgadza się! Proszę spróbuj ponownie.',
                  category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Zostałeś wylogowany", category='info')
    return redirect(url_for("home_page"))


@app.route("/ip", methods=["GET"])
def ip():
    return jsonify({'ip': request.remote_addr}), 200

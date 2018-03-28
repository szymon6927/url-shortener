from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Users

@auth.route('/allusers')
@login_required
def all_users():
    """
    Render the all users
    """
    users = Users.query.all()

    return render_template('auth/all_users.html', title="Tabela wszystkich zarejestrowanych użytkowników",
                           users=users)


@auth.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(email=form.email.data,
                     username=form.username.data,
                     first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('Pomyślnie utworzono użytkownika, przejdź do sekcji logowania.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        user = Users.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log user in
            login_user(user)

            # redirect to the dashboard page after login
            return redirect(url_for('home.homepage'))

        # when login details are incorrect
        else:
            flash('Zły e-mail lub hasło.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('Pomyślnie wylogowano użytkownika')

    # redirect to the login page
    return redirect(url_for('auth.login'))

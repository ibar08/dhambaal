from flask import Blueprint, render_template, url_for, redirect, flash
from dhambaal.auth.model import User
from dhambaal.auth.forms import LoginForm, RegisterForm
from flask_bcrypt import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__, template_folder="templates")

#Register Route

@auth.route("/dashboard/user/register", methods=['POST','GET'])

def register_user():
    form = RegisterForm()
    #! Remove Later
    #user =User()
    if form.validate_on_submit():
        #if user 1 is already logged in we need to redirect to dashboard
        # TODO 1 : check if admin or staff
        # if username or email is already taken display error message

        if User.validate_email(form.email.data):
            flash("Email Already exist, Please choose different", "is-warning")
            return redirect(url_for("auth.register_user"))
        
        if User.validate_username(form.username.data):
            flash("Username Already exist, Please choose different", "is-warning")
            return redirect(url_for("auth.register_user"))
        user =User(name=form.name.data,email=form.email.data,
                    username=form.username.data,password = generate_password_hash(form.password.data).decode("utf-8"))
        user.save()
        flash("User created successfully", 'is-success')
        return redirect(url_for("auth.users"))
    return render_template("register.html",form=form)

@auth.route("/dashboard/users")
def users():
    users= User.query.all()
    return render_template("users.html", users=users)

@auth.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        # TODO1 : Compare hashed password with users password
        # TODO2. Check if email and password match
        #  User login
        flash("Logged in successfully", 'is-success')
        return redirect(url_for("dashboard.index"))
    return render_template("login.html", form=form)
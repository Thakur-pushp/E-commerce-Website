from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from database import *

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/register')
def register():
    return render_template('register.html')

@auth_bp.route('/log', methods=["POST"])
def authentication():
    user_id = request.form['email'].strip()
    password = request.form['password'].strip()

    connect = get_connection()
    pas = connect.execute("SELECT password, name FROM user WHERE user_id = ?",(user_id,)).fetchone()
    connect.close()
    username = pas[1]

    if pas is None:
        flash("User Not Exists, Please Register!")
        return redirect(url_for('auth.login'))
    else:
        pas = pas[0]
        if password == pas:
            session['user_id'] = user_id
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash("Wrong Password, Please try again!")
            return redirect(url_for('auth.login'))


@auth_bp.route('/reg', methods=["POST"])
def authentication_reg():
    name = request.form.get('fullname', '').strip()
    user_id = request.form['email'].strip()
    password = request.form['password'].strip()

    connect = get_connection()
    db_name = connect.execute("SELECT name FROM user WHERE user_id = ?",(user_id,)).fetchone()

    if db_name is not None:
        flash(f"{db_name[0]}, You are already our Customer!")
        return redirect(url_for('auth.register'))
    else:
        connect.execute("""
            INSERT INTO user(user_id, name, password)
            VALUES (?,?,?)
        """,(user_id,name,password))
        connect.commit()
        connect.close()
        return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for('home'))

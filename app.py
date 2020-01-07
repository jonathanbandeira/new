from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, g, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('hello.html')
    
@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        return render_template('session.html')
    return index()

@app.route('/password_reset')
def reset():
    return render_template('password_reset.html')

@app.route('/register')
def other():
    return render_template('register.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=8000)
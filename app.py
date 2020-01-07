from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, g, url_for
import os

from flask_wtf import CsrfProtect
import json

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('hello.html')
    
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        return render_template('session.html')
    return index()

#@app.route('/login', methods=['GET', 'POST'])
#def do_admin_login():
#   create_form = forms.CreateForm(request.form)
    
 #   if request.method== 'POST' and create_form.validate():
        
  #    user = User(username = create_form.username.data,
   #               password = create_form.password.data,
    #              email = create_form.email.data )
      
#      db.session.add(user)
 #     db.session.commit()
      
  #    sucess_message = 'Usuário registrado na base de dados!'
   #   flash(sucess_message)
      
  #  return render_template('create.html', form = create_form)
    
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
    app.run(debug=True,host='0.0.0.0', port=8000)
from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

    
@app.route('/index')
def index():
  user = { 'name' : 'Forrest' }
  locations = [
  {
    'location' : '2883 Sunny Wood Cir., Santa Rosa, CA',
    'duration' : '20 minutes'
  },
  {
    'location' : '1536 48th Ave., San Francisco, CA',
    'duration' : '20 minutes'
  }
  ]
  return render_template("index.html", 
    title = 'Home',
    user = user,
    locations = locations)
  
@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for: ' + form.openid.data + '. Remember me: ' + str(form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', 
    title = 'Sign In',
    form = form,
    providers = app.config['OPENID_PROVIDERS'])
from flask import render_template
from app import app
from forms import LoginForm

@app.route('/')

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
  
@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', 
    title = 'Sign In',
    form = form)
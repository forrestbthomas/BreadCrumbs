from flask import render_template, flash, redirect, request
from app import app, db, models
from forms import LoginForm
import inspect, datetime

@app.route('/coords', methods = ['POST'])
def coords():
  lat = request.form['latitude']
  lon = request.form['longitude']
  coords = str(lat) + ', ' + str(lon)

  u = models.User(name='Forrest Thomas', email='forrestbthomas@gmail.com')
  db.session.add(u)
  user = models.User.query.get(1)

  d = models.Date(date=str(datetime.date.today()), user_id=user.id)
  db.session.add(d)
  date = models.Date.query.get(1)

  l = models.Location(location=coords, date_id=date.id)
  db.session.add(l)
  location = models.Location.query.get(1)

  t = models.Time(time=str(datetime.datetime.now().time), location_id=location.id)
  db.session.add(t)
  time = models.Time.query.get(1)

  db.session.commit()
  return 'success'

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
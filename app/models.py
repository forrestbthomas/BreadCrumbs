from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(64), index = True, unique = True)
  email = db.Column(db.String(120), index = True, unique = True)
  dates = db.relationship('Date', backref = 'author', lazy = 'dynamic')
  
  def __repr__(self):
    return '<User %r>' % (self.name)

class Date(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  date = db.Column(db.String(64), index = True, unique = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

  def __repr__(self):
        return '<Date %r>' % (self.date)

class Location(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  location = db.Column(db.String(120), index = True, unique = True)
  date_id = db.Column(db.String(64), db.ForeignKey('date_id'))

  def __repr__(self):
        return '<Location %r>' % (self.location)

class Time(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  time = db.Column(db.String(64), index = True, unique = True)
  location_id = db.Column(db.String(120), db.ForeignKey('location_id'))

  def __repr__(self):
        return '<Time %r>' % (self.time)

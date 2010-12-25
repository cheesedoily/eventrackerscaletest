from google.appengine.ext import db

class Counter(db.Model):
    obj = ReferenceProperty() # generic reference
    count_one = db.IntergerProperty() 
    count_two = db.IntergerProperty()
    count_three = db.IntergerProperty()
    count_four = db.IntergerProperty()
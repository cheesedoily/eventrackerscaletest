from google.appengine.ext import db

class Counter(db.Model):
    dimension_one = db.ReferenceProperty(collection_name="dim_one_counters") # generic reference
    dimension_two = db.ReferenceProperty(collection_name="dim_two_counters") # generic reference
    date_hour = db.DateTimeProperty()
    count_one = db.IntegerProperty() 
    count_two = db.IntegerProperty()
    count_three = db.IntegerProperty()
    count_four = db.IntegerProperty()
import logging

from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from account.models import Account

# campaign
class DimensionOneLevelOne(db.Model):
    pass
    
# adgroup    
class DimensionOneLevelTwo(db.Model):
    pass

# creative
class DimensionOneLevelThree(db.Model):
    pass
    
# application
class DimentionTwoLevelOne(db.Model):
    pass

# adunit (slot)
class DimentionTwoLevelTwo(db.Model):
    pass

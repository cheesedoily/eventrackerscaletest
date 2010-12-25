import logging

from google.appengine.ext import db



# campaign
class DimensionOneLevelThree(db.Model):
    @classmethod
    def key_from_key_name(cls,key_name):
        return db.Key.from_path(cls.kind(),key_name)
    
# adgroup    
class DimensionOneLevelTwo(DimensionOneLevelThree):
    level_above = db.ReferenceProperty(DimensionOneLevelThree)
    
# creative
class DimensionOneLevelOne(DimensionOneLevelThree):
    level_above = db.ReferenceProperty(DimensionOneLevelTwo)
    
# app
class DimentionTwoLevelTwo(DimensionOneLevelThree):
    pass
    
# adunit (slot)
class DimentionTwoLevelOne(DimensionOneLevelThree):
    level_above = db.ReferenceProperty(DimentionTwoLevelTwo)
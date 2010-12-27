import logging

from google.appengine.ext import db

class DimensionOneLevelThree(db.Model):
    @classmethod
    def key_from_key_name(cls,key_name):
        return db.Key.from_path(cls.kind(),key_name)
    
class DimensionOneLevelTwo(DimensionOneLevelThree):
    level_above = db.ReferenceProperty(DimensionOneLevelThree)
    
class DimensionOneLevelOne(DimensionOneLevelThree):
    level_above = db.ReferenceProperty(DimensionOneLevelTwo)
    
class DimensionTwoLevelTwo(DimensionOneLevelThree):
    pass
    
class DimensionTwoLevelOne(DimensionOneLevelThree):
    level_above = db.ReferenceProperty(DimensionTwoLevelTwo)
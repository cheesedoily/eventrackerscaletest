import logging
import random

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.api import memcache
from google.appengine.api.taskqueue import Task

class LogEventOne(webapp.RequestHandler):
    def get(self):
        attributes = ['uid','dim2l1','t','req','dim1l1','imp']    
        params = {}
        for attr in attributes:
            params.update({attr:self.request.get(attr,None)})
        log(**params)
        self.response.out.write('I AM LOGGING')
        
        
class LogEventThree(webapp.RequestHandler):
    def get(self):
        pass
        
def log(**kwargs): 
    # THIS IS WHERE ALL THE HEAVY LIFTING IS DONE                   
    logging.info("I AM LOGGING: %s"%kwargs)
    
    # Put the logging info into memecache
    # The key should be based on a incrementing the index for this instance
    # k<instance_id><index>
    # the index value can either be stored as a global for the instance 
    # or as a entry in memecache with key k<instance_id>
    
    # After N writes to memecache we should sent out a Task like this
    t = Task(params={'start':0,'length':100, 'instance_id':instance_id},method='GET')
    t.add('bulk-log-processor')
    

application = webapp.WSGIApplication([('/log/one', LogEventOne),
                                      ('/log/three',LogEventThree), 
                                     ],
                                     debug=True)

def main():
    # attaches a process id to the instance
    # TODO: make sure this is unique, probably with a memcache list or counter    
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    
    
pid = globals().get("instance_id",None)
if not pid:
    globals()["instance_id"] = random.randint(1,1e6) # one in a million
    
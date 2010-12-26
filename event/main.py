import random
import time
import os
import logging

import urllib
import urllib2

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
from google.appengine.api import namespace_manager


from event.models import DimensionOneLevelOne
from async.main import log

class EventOne(webapp.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        uid = self.request.get("uid")
        dim_two_level_one = self.request.get("id")
        # v1 = self.response.get("k1")
        # v2 = self.response.get("k1")
        # TODO: get vhost
        # vhost = asdf
        logging.info("instance_id: %s"%instance_id)
        t = time.time()
        
        request_id = "%s:%s:%s"%(t,uid,dim_two_level_one)
        
        # 90 percent of the time we attach information to the request
        if random.randint(0,9) != 0:
            # level3:level2:level1
            dim_one_level_one_key_name = "k:%s:%s:%s"%(random.randint(0,9),random.randint(0,9),random.randint(0,9)) 
            dim_one_level_one = str(DimensionOneLevelOne.key_from_key_name(dim_one_level_one_key_name))
        else:
            dim_one_level_one_key_name = None
            dim_one_level_one = None
                
        
        logging_params = {"uid":uid,"dim2l1":dim_two_level_one,"t":t,"req":request_id}
        if dim_one_level_one:
            imp_id = request_id + ":" + str(dim_one_level_one)
            logging_params.update(dim1l1=dim_one_level_one_key_name,imp=imp_id)
            
        if self.request.get("local","0") == "0":
            deadline = self.request.get("deadline")
            deadline = float(deadline) if deadline else None    
            rpc = urlfetch.create_rpc(deadline=deadline) 
            data = urllib.urlencode(logging_params)
            # url = "http://eventrackerscaletest.appspot.com/log/one"
            url = "http://localhost:8081/log/one"
            logging.info("URL: %s with deadline: %s"%(url+"?"+data,deadline))
            urlfetch.make_fetch_call(rpc,url+"?"+data)

            try:
                result = rpc.get_result()
                if result.status_code == 200:
                    html = result.content
                else:
                    html = "ERROR"    
            except urlfetch.DownloadError:
                html = None
        else:
            log(**logging_params)        
            html = "LOGGED"
            
        self.response.out.write('<html><head/><body><b>Hello, webapp World! %s %s %s %s <br/> %s <br/> %s </b></body></html>'%(request_id,dim_two_level_one,uid,t,logging_params, html))
        

class EventTwo(webapp.RequestHandler):
    def get(self):
        pass    
        
class EventThree(webapp.RequestHandler):
    pass        

application = webapp.WSGIApplication([('/event/one', EventOne),
                                      ('/event/two', EventTwo),
                                      ('/event/three',EventThree), 
                                     ],
                                     debug=True)

def main():
    # attaches a process id to the instance
    # TODO: make sure this is unique, probably with a memcache list
    pid = globals().get("instance_id",None)
    if not pid:
        globals()["instance_id"] = random.randint(1,1e6) # one in a million
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
import random
import time

import urllib
import urllib2

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch


class EventOne(webapp.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        uid = self.request.get("uid")
        dim_two_level_one = self.request.get("id")
        # v1 = self.response.get("k1")
        # v2 = self.response.get("k1")
        # TODO: get vhost
        # vhost = asdf
        t = time.time()
        
        request_id = "%s:%s:%s"%(t,uid,dim_two_level_one)
        
        # 90 percent of the time we attach information to the request
        if random.randint(0,9) != 0:
            dim_one_level_one = random.randint(0,100) 
        else:
            dim_one_level_one = None
                
        
        logging_params = {"uid":uid,"dim2l1":dim_two_level_one,"t":t,"req":request_id}
        if dim_one_level_one:
            imp_id = request_id + ":" + str(dim_one_level_one)
            logging_params.update(dim1l1=dim_one_level_one,imp=imp_id)
            
        data = urllib.urlencode(logging_params)
        url = "http://localhost:8081/log/one"
        response = urlfetch.fetch(url+"?"+data)
        html = response.content

        self.response.out.write('<html><head/><body><b>Hello, webapp World! %s %s %s %s <br/> %s</b></body></html>'%(request_id,dim_two_level_one,uid,t,html))
        

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
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
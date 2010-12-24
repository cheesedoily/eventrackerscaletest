from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class EventOne(webapp.RequestHandler):
    def get(self):
        self.response.out.write('I AM LOGGING')
        

class EventTwo(webapp.RequestHandler):
    def get(self):
        pass    
        
class EventThree(webapp.RequestHandler):
    pass        

application = webapp.WSGIApplication([('/log/one', EventOne),
                                      ('/log/two', EventTwo),
                                      ('/log/three',EventThree), 
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
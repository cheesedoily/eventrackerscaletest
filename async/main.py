from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class LogEventOne(webapp.RequestHandler):
    def get(self):
        # THIS IS WHERE ALL THE HEAVY LIFTING SHOULD BE DONE
        self.response.out.write('I AM LOGGING')
        
class LogEventThree(webapp.RequestHandler):
    def get(self):
        pass            

application = webapp.WSGIApplication([('/log/one', LogEventOne),
                                      ('/log/three',LogEventThree), 
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
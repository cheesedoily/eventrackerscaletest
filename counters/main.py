from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class TestHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('THESE ARE THE COUNTERS')
        

application = webapp.WSGIApplication([('/counter/test', TestHandler),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
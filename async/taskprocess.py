import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.api import memcache
from google.appengine.api.taskqueue import Task

from counters.models import Counter

class LogTaskHandler(webapp.RequestHandler):
    def get(self):
        logging.info("I AM PROCESSING A TASK")
        # update a list of counters across the various dimensions

application = webapp.WSGIApplication([('/_ah/queue/bulk-log-processor', LogTaskHandler),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
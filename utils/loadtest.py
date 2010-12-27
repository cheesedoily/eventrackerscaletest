#    Copyright 2009 Google Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Simple web application load testing script.

This is a simple web application load
testing skeleton script. Modify the code between !!!!!
to make the requests you want load tested.
"""



import httplib2
import random
import socket
import time
import uuid
import sys
import os

sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/django")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/webob")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/yaml/lib")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/fancy_urllib")
sys.path.append('/'.join(os.getcwd().split("/")[:-1]))
sys.path.append('.')

from threading import Event
from threading import Thread
from threading import current_thread
from urllib import urlencode

from event.models import DimensionTwoLevelOne
from event.models import db




# Modify these values to control how the testing is done

# How many threads should be running at peak load.
NUM_THREADS = 50

# How many minutes the test should run with all threads active.
TIME_AT_PEAK_QPS = 1 # minutes

# How many seconds to wait between starting threads.
# Shouldn't be set below 30 seconds.
DELAY_BETWEEN_THREAD_START = 5 # seconds

quitevent = Event()

def threadproc():
    """This function is executed by each thread."""
    print "Thread started: %s" % current_thread().getName()
    h = httplib2.Http(timeout=30)
    while not quitevent.is_set():
        try:
            # HTTP requests to exercise the server go here
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            
            uid = uuid.uuid4()
            key_name = "k:%02d:%02d"%(random.randint(0,9),random.randint(0,9))
            dim_two_level_one = db.Key.from_path('DimensionTwoLevelOne',key_name,_app='eventrackerscaletest')
            
            url = "http://eventrackerscaletest.appspot.com/event/one?deadline=.008&uid=%s&id=%s"%(uid,dim_two_level_one)
            resp, content = h.request(url)
            # print url  
            if resp.status != 200:
                print "Response not OK"
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        except socket.timeout:
            pass

    print "Thread finished: %s" % current_thread().getName()


if __name__ == "__main__":
    runtime = (TIME_AT_PEAK_QPS * 60 + DELAY_BETWEEN_THREAD_START * NUM_THREADS)
    print "Total runtime will be: %d seconds" % runtime
    threads = []
    try:
        for i in range(NUM_THREADS):
            t = Thread(target=threadproc)
            t.start()
            threads.append(t)
            time.sleep(DELAY_BETWEEN_THREAD_START)
        print "All threads running"
        time.sleep(TIME_AT_PEAK_QPS*60)
        print "Completed full time at peak qps, shutting down threads"
    except:
        print "Exception raised, shutting down threads"

    quitevent.set()
    time.sleep(3)
    for t in threads:
        t.join(1.0)
    print "Finished"
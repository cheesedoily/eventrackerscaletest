#!/usr/bin/python
import code
import getpass
import sys

# sys.path.append("~/google_appengine")
# sys.path.append("~/google_appengine/lib/yaml/lib")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/yaml/lib")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/fancy_urllib")



from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db

def auth_func():
    return "appenginescaletest@gmail.com", "1234test1234"
    return raw_input('Username:'), getpass.getpass('Password:')

if len(sys.argv) < 2:
    print "Usage: %s app_id [host]" % (sys.argv[0],)
app_id = sys.argv[1]
if len(sys.argv) > 2:
    host = sys.argv[2]
else:
    host = '%s.appspot.com' % app_id

remote_api_stub.ConfigureRemoteDatastore(app_id, '/remote_api', auth_func, host)

from event.models import DimensionOneLevelThree, DimensionOneLevelTwo, DimensionOneLevelOne
from event.models import DimentionTwoLevelTwo, DimentionTwoLevelOne

# dims3 = []
# for i in range(10):
#     dim3 = DimensionOneLevelThree(key_name="k:%02d"%i)
#     dims3.append(dim3)
#     dims2 = []
#     for j in range(10):
#         dim2 = DimensionOneLevelTwo(key_name="k:%02d:%02d"%(i,j),level_above=dim3)
#         dims2.append(dim2)
#         dims1 = []
#         for k in range(10):
#             dim1 = DimensionOneLevelOne(key_name="k:%02d:%02d:%02d"%(i,j,k),level_above=dim2)
#             dims1.append(dim1)
#         print "putting dims1 for dim3:%02d dim2:%02d"%(i,j)    
#         db.put(dims1)
#     print "putting dim2 for dim3:%02d"%i    
#     db.put(dims2)
# print "putting dims3"    
# db.put(dims3)            

# dims2 = []
# for i in range(10):
#     dim2 = DimentionTwoLevelTwo(key_name="k:%02d"%i)
#     dims2.append(dim2)
#     dims1 = []
#     for j in range(10):
#         dim1 = DimentionTwoLevelOne(key_name="k:%02d:%02d"%(i,j),level_above=dim2)
#         dims1.append(dim1)
#     print "putting dim1 for dim2:%02d"%i    
#     db.put(dims1)
# print "putting dims2"    
# db.put(dims2)            


code.interact('App Engine interactive console for %s' % (app_id,), None, locals())
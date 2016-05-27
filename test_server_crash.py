from subprocess import call
import os
import time
import xmlrpclib
from xmlrpclib import Binary
#SERVER CRASH
port = '5001'
server = 'http://localhost:'+port
rpct = xmlrpclib.ServerProxy(server)
print "Terminating server on port:"+port
rpct.terminate()
print "Restarting the dataserver on port:"+port+" in 1 seconds"
time.sleep(1)
os.system('xterm -hold -e "python dataserver.py 5001 5002 5003"')

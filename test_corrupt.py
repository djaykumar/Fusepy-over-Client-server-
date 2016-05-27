from subprocess import call
import os
import time
import xmlrpclib
from xmlrpclib import Binary
# os.system('open -a Terminal "`pwd`"')
port = '5001'
server = 'http://localhost:'+port
rpct = xmlrpclib.ServerProxy(server)
#SERVER CORRUPTION
print "List of contents",rpct.list_contents()
key = rpct.list_contents()
print "Corrupt a Key",key[1]
rpct.corrupt(Binary(key[1]))
print "Corruption injected in server with port:"+port
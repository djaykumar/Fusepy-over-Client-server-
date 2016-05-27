from subprocess import call
import os
import time
import xmlrpclib
from xmlrpclib import Binary
# os.system('open -a Terminal "`pwd`"')
port = '5001'
server = 'http://localhost:'+port
rpct1 = xmlrpclib.ServerProxy(server)
rpct2 = xmlrpclib.ServerProxy('http://localhost:5002')
rpct3 = xmlrpclib.ServerProxy('http://localhost:5003')
#SERVER CORRUPTION
print "List of contents in server1",rpct1.list_contents()
print "List of contents in server2",rpct2.list_contents()
print "List of contents in server3",rpct3.list_contents()
key1 = rpct1.list_contents()
key2 = rpct2.list_contents()
key3 = rpct3.list_contents()
print "Corrupting key in multiple servers with port: 5001,5002,5003"
rpct1.corrupt(Binary(key1[1]))
rpct2.corrupt(Binary(key2[1]))
rpct3.corrupt(Binary(key3[1]))
print "Corruption injected in multiple servers with port: 5001,5002,5003"
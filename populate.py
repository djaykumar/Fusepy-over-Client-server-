from subprocess import call
import os
import time
import xmlrpclib
from xmlrpclib import Binary
for i in range(10):
	os.system('echo hello > /home/rxavier/pocsd/final/fusemount/hello'+str(i)+'.txt &')

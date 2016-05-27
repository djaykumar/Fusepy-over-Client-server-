from subprocess import call
import os
import time
sleep_time = 1
# os.system('open -a Terminal "`pwd`"')
os.system('xterm -hold -e "python metaserver.py 5000" &')
time.sleep(sleep_time)
os.system('xterm -hold -e "python dataserver.py 5001 5002 5003" &')
time.sleep(sleep_time)
os.system('xterm -hold -e "python dataserver.py 5002 5003 5001" &')
time.sleep(sleep_time)
os.system('xterm -hold -e "python dataserver.py 5003 5001 5002" &')
time.sleep(2*sleep_time)
os.system('xterm -hold -e "python FileSystem.py fusemount 3 3 http://localhost:5000 http://localhost:5001 http://localhost:5002 http://localhost:5003"')

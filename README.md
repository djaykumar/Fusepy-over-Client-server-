# Fusepy-over-Client-server-
#Python implementation of a user space Filesytem on Client Server Architecture
implementation built over Open Source userspace Filesystem implementation Fuse
Fuse has been modified to work as a hierarchichal filesystem instead of a flat one
Filesystem.py- python file that contains the function calls of the filesystem
Data and metadata of every file and directory is stored in separate servers called data server and meta server
Filesystem.py runs on client, Dataserver.py runs on data servers and metaserver.py runs on metaservers
The server implementations are modified versions of SimpleHT implementations
There are multiple dataservers and a single metaserver. Filesystem.py accesses filesystem data and metadata through RPC's (remote procedure calls)
populate.py is used for populating the filesystem
run_3servers.py is used for running 3 dataservers and 1 metaserver
Filesystem can handle server crashses and data corruption
to test the implementation for the faults test_corrupt.py, test_multiple_corrupt.py and test_server_crash.py can be used

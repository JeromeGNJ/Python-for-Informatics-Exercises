import os
from os.path import join
import hashlib
d = {}
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.mp3'):
            
            thefile = os.path.join(dirname,filename)
            size = os.path.getsize(thefile)
            fhand = open(thefile,'r')
            data = fhand.read()
            fhand.close()
            checksum = hashlib.md5(data).hexdigest()
            if checksum in d:
                print d[checksum],thefile
            else:
                d[checksum] = thefile


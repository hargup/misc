import subprocess
import shlex
import os
from sys import stdout

# mp4_files = ipython.magic('!ls | grep mp4')
mp4_files = [x for x in os.listdir('.') if ".mp4" in x]
m4a_files = [x.rstrip('.mp4') + '.m4a' for x in mp4_files]
for mp4, m4a in zip(mp4_files, m4a_files):
    cmd = "ffmpeg -i %s -vn -acodec \'copy\' %s" % (shlex.quote(mp4),
                                                    shlex.quote(m4a))
    subprocess.call(shlex.split(cmd), stdout=stdout)

import os, time, sys

path = r"c:\users\%myusername%\downloads"

now = time.time()

for f in os.listdir(path):
 f = os.path.join(path, f)
 if os.stat(f).st_mtime < now - 7 * 86400:

  if os.path.isfile(f):

   os.remove(os.path.join(path, f))

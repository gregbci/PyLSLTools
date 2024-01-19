import time
from pylsl import StreamInlet, ContinuousResolver

resolver = ContinuousResolver()

while True:
   time.sleep(2)

   streams = resolver.results()
   num = len(streams)
   if num > 0:
      print("found ", num, " streams")
   else:
      print("no streams")


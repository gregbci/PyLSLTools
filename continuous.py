import time
from pylsl import StreamInlet, ContinuousResolver

resolver = ContinuousResolver("name", "Unity.Pose")


while True:
   time.sleep(2)

   streams = resolver.results()
   num = len(streams)
   if num > 0:
      print("found ", num, " streams")
      inlet = StreamInlet(streams[0])

      while True:
         # read from inlet and print, this will infinite loop
         sample, timestamp = inlet.pull_sample()
         print(timestamp, sample)
   else:
      print("no streams")




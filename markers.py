import random
import time

from pylsl import StreamInfo, StreamOutlet

# Generate markers that Bessy can read
info = StreamInfo('LSL Test', 'LSL_Marker_Strings', 1, channel_format="string")

# next make an outlet
outlet = StreamOutlet(info)

print("now sending data...")
while True:
    
    mysample = ["mi,2,0,2"]

    # now send it and wait for a bit
    outlet.push_sample(mysample)
    time.sleep(5.0)

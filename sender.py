"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import random
import time

from pylsl import StreamInfo, StreamOutlet

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover).
#info = StreamInfo('GregSender', 'EEG', 3, 10, 'float32')
#info = StreamInfo('Unity.Pose', 'Unity.Transform', 3, 10, 'float32')
info = StreamInfo('LSL Test', 'LSL_Marker_Strings', 1, channel_format="float32")

# next make an outlet
outlet = StreamOutlet(info)
count = 0

print("now sending data...")
while True:
    mysample = [count]
    count += 1

    # now send it and wait for a bit
    outlet.push_sample(mysample)
    time.sleep(1)

"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_byprop

print("looking for a stream...")
#streams = resolve_byprop("type", "EEG", timeout=5.0)
streams = resolve_byprop("type", "LSL_Marker_Strings", timeout=10.0)

# create a new inlet to read from the stream
print("found", streams.count(0), "streams")
inlet = StreamInlet(streams[0])

while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)

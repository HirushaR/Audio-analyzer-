import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib tk

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels =CHANNELS,
    rate = RATE,
    input =True,
    output = True,
    frames_per_buffer =CHUNK
)

fig, ax = plt.subplots()
x = np.arange(0, 2* CHUNK, 2)
line, = ax.plot(x,np.random.rand(CHUNK))
num_plots = 0
while True:
    data= stream.read(CHUNK)
    #print(data)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 127
    # print(data_int)
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
    num_plots += 1
print(num_plots)



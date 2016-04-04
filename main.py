from uuid import getnode as getID
import pyaudio
import sys
import math
from __future__ import division

id = getID()

#Used the pyaudio examples to write the code
rate = float(16000)

p = pyaudio.PyAudio()
stream = p.open(format=paInt16, channels=1, rate=rate, output=True)

def playTone(frequency, duration):
    samplePerCycle = rate / frequency
    data = ""
    for i in range(rate * duration):
        num = 32767 * math.sin(math.pi * 2 * (i % samplePerCycle) / samplePerCycle)
        data = data + char(int(num))
    stream.write(data)

def close():
    stream.stop_stream()
    stream.close()
    p.terminate()

def 

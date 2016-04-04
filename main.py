from uuid import getnode as getID
import pyaudio
import sys
import math
from __future__ import division

id = getID()

rate = float(16000)

p = pyaudio.PyAudio()
stream = p.open(format=paInt16, rate=rate, output=True)

def playTone(frequency, duration):
    samplePerCycle = rate / frequency
    for i in range(rate * duration):
        num = 32767 * math.sin(math.pi * 2 * (i % samplePerCycle) / samplePerCycle)
        data = data + char(int(num))
    
def 

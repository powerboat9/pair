from uuid import getnode as getID
import pyaudio
import sys
import math
from __future__ import division

id = getID()

p = pyaudio.PyAudio()

def playTone(frequency, duration):
    rate = 16000

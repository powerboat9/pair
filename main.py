from uuid import getnode as getID
import pyaudio
import sys
import math
from __future__ import division

id = getID()

#Used the pyaudio examples to write the code
rate = float(16000)

baseFrequency = 18000
binSize = 16

def getBase(channel):
    return baseFrequency + 16 * binSize * channel

def getToneData(frequency, duration):
    samplePerCycle = rate / frequency
    data = ""
    for i in range(rate * duration):
        num = 32767 * math.sin(math.pi * 2 * (i % samplePerCycle) / samplePerCycle)
        data = data + char(int(num))
    return data

p = pyaudio.PyAudio()
stream = p.open(format=paInt16, channels=1, rate=rate, output=True)

def playData(data):
    stream.write(data)

def playTone(frequency, duration)
    data = getToneData(frequency, duration)
    playData(data)

def mixTones(tone1, tone2):
    data = ""
    if tone2 > tone1:
        tone1 = padEnd(tone1, len(tone2))
    elif tone1 > tone2:
        tone2 = padEnd(tone2, len(tone1))
    for i in range(len(tone1)):
        char1 = ord(tone1[i]) / 2
        char2 = ord(tone2[i]) / 2
        data = data + char(char1 + char2)
    return data

def close():
    stream.stop_stream()
    stream.close()
    p.terminate()

bands = {"isOn": 0; "sendByte": 1, "send":9, "ready":10, "done":11}
sending = array()

def forceBinnary(n)
    if (n == 0) or (n == 1):
        return True
    else:
        return False

def createSetting(name, value)
    if (name == "isOn") or (name == "send") or (name == "ready") or (name == "done"):
        ok = forceBinnary(value)
        if not ok:
            return False
        sending[bands[name]] = value
    elif (name == "sendByte"):
        bits = "{0:b}".format(value)
        if len(bits) > 8:
            return False
        elif len(bits) < 8:
            bits = ("0" * (8 - len(bits))) + bits
        for i in range(8):
            sending[bands["sendByte"] + i] = bits[8 - i - 1]
    return True
            
def getMessage():
    

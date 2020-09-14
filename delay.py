# Title: EE 321 Project 1: Audio Manipulation. Part I: Delay
# Purpose: To implement a delay into an audio file, in this case a .wav file
# Developers: Cameron Palmer, Shawn Boyd, Siddesh Sood
# Last Modified: September 13, 2020

import matplotlib.pyplot as plt
import numpy as np
import wave
from playsound import playsound as ps
import sys

# Open the wave file to read from
audio = wave.open("EE321audio.wav", "r")

# Print out some basic information about our original audio file
print("\n//////////////////Info for original audio file//////////////////")
print("Number of channels (1 for mono, 2 for stereo): " + str(audio.getnchannels()))
print("Sample rate: " + str(audio.getframerate()))
print("Total number of frames: " + str(audio.getnframes()))
print("Length: " + str(round(audio.getnframes()/audio.getframerate(), 2)) + "s")
print("Sample width: " + str(audio.getsampwidth()) + " bytes, or " + str(audio.getsampwidth()*8) + " bits")
print("////////////////////////////////////////////////////////////////\n")

# Open the wave file we'll create to store the original audio file converted to mono
audioOut = wave.open("audioOut.wav", "w")
audioOut.setnchannels(2)
audioOut.setsampwidth(2)
audioOut.setframerate(44100)

# Play the original audio as a test
ps("EE321audio.wav")

# Get the raw audio from the wave file
signal = audio.readframes(-1)

signal = np.fromstring(signal, "Int16")
framerate = audio.getframerate()



signalarray = bytearray(signal)
zerosarray = bytearray(441000)

signalarray[0:0] = zerosarray

#print(signalarray)


# Write out the new audio
audioOut.writeframes(signalarray)

Time = np.linspace(0, len(signal)/framerate, num=len(signal))

plt.figure(1)
plt.title("Original Audio")
plt.plot(Time, signal)
plt.show()


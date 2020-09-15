# Title: EE 321 Project 1: Audio Manipulation. Part I: Delay
# Purpose: To implement a delay into an audio file, in this case a .wav file
# Developers: Cameron Palmer, Shawn Boyd, Siddesh Sood
# Last Modified: September 13, 2020

import matplotlib.pyplot as plt
import numpy as np
import wave
from playsound import playsound as ps
import sys

#print(sys.byteorder)
# Open the wave file to read from
audio = wave.open("EE321audio.wav", "r")

# Play the original audio as a test
#ps("EE321audio.wav")

# Print out some basic information about our original audio file
print("\n//////////////////Info for original audio file//////////////////")
print("Number of channels (1 for mono, 2 for stereo): " + str(audio.getnchannels()))
print("Sample rate: " + str(audio.getframerate()))
print("Total number of frames: " + str(audio.getnframes()))
print("Length: " + str(round(audio.getnframes()/audio.getframerate(), 2)) + "s")
print("Sample width: " + str(audio.getsampwidth()) + " bytes, or " + str(audio.getsampwidth()*8) + " bits")
print("////////////////////////////////////////////////////////////////\n")

# Open the wave files we'll create to store the original audio file with different delays
audioOut0 = wave.open("delay1.wav", "w")
audioOut0.setnchannels(2)
audioOut0.setsampwidth(2)
audioOut0.setframerate(44100)

audioOut1 = wave.open("delay2.wav", "w")
audioOut1.setnchannels(2)
audioOut1.setsampwidth(2)
audioOut1.setframerate(44100)

audioOut2 = wave.open("delay3.wav", "w")
audioOut2.setnchannels(2)
audioOut2.setsampwidth(2)
audioOut2.setframerate(44100)

# Define a constant to use when implementing delays, in bytes/sec
SAMPLERATE = audio.getframerate()
SAMPLEWIDTH = audio.getsampwidth()
NUMCHANNELS = audio.getnchannels()
BYTESINASEC =  SAMPLERATE * SAMPLEWIDTH * NUMCHANNELS
print(BYTESINASEC)


# Get the raw audio from the wave file and convert it to an ndarray
signal = audio.readframes(-1)
signal = np.frombuffer(signal, "Int16", -1)

# Convert the ndarray into a bytearray so we can add a delay in the front of it
signalarray = bytearray(signal)

# Create the delays of type bytearray
zerosarray1sec = bytearray(BYTESINASEC)
zerosarray3sec = bytearray(BYTESINASEC*3)
zerosarray5sec = bytearray(BYTESINASEC*5)

# Add in the delays and write out the delayed files
signalOut0 = zerosarray1sec + signalarray
signalOut0 = np.frombuffer(signalOut0, "Int16", -1)
audioOut0.writeframes(signalOut0)

signalOut1 = zerosarray3sec + signalarray
signalOut1 = np.frombuffer(signalOut1, "Int16", -1)
audioOut1.writeframes(signalOut1)

signalOut2 = zerosarray5sec + signalarray
signalOut2 = np.frombuffer(signalOut2, "Int16", -1)
audioOut2.writeframes(signalOut2)

#audioIn0 = wave.open("delay1.wav", 'r')
#signalIn0 = audioIn0.readframes(-1)
#signalIn0 = np.frombuffer(signalIn0, "Int")
## Graphs

#print(signalOut0)
# The time variable for the horizontal axis of the original audio
Time = np.linspace(0, len(signal)/SAMPLERATE, num=len(signal))
Time0 = np.linspace(0, len(signalOut0)/SAMPLERATE, num=len(signalOut0))
Time1 = np.linspace(0, len(signalOut1)/SAMPLERATE, num=len(signalOut1))
Time2 = np.linspace(0, len(signalOut2)/SAMPLERATE, num=len(signalOut2))

# Graph of original audio
plt.figure(1)
plt.title("Original Audio")
plt.plot(Time/NUMCHANNELS, signal/NUMCHANNELS)
plt.show()

# Graph of 1st delayed audio
plt.figure(2)
plt.title("Audio with 1s delay")
plt.plot(Time0/NUMCHANNELS, signalOut0/NUMCHANNELS)
plt.show()

# Graph of 2nd delayed audio
plt.figure(3)
plt.title("Audio with 3s delay")
plt.plot(Time1/NUMCHANNELS, signalOut1/NUMCHANNELS)
plt.show()

# Graph of 3rd delayed audio
plt.figure(4)
plt.title("Audio with 5s delay")
plt.plot(Time2/NUMCHANNELS, signalOut2/NUMCHANNELS)
plt.show()a




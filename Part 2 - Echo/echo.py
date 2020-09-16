# Title: EE 321 Project 1: Audio Manipulation. Part II: Echo
# Purpose: To implement echoes into a .wav audio file
# Developers: Cameron Palmer, Shawn Boyd, Siddesh Sood
# Last Modified: September 15, 2020

import matplotlib.pyplot as plt
import numpy as np
import wave

# Open the wave file to read from
audio = wave.open("originalAudio.wav", "r")

# Defining some constants to use for processing the audio
SAMPLERATE = audio.getframerate()
SAMPLEWIDTH = audio.getsampwidth()
TOTALFRAMES = audio.getnframes()
NUMCHANNELS = audio.getnchannels()
BYTESINASEC = SAMPLERATE * SAMPLEWIDTH * NUMCHANNELS

# Print out some basic information about our original audio file
print("\n//////////////////Info for original audio file//////////////////")
print("Number of channels (1 for mono, 2 for stereo): " + str(NUMCHANNELS))
print("Sample rate: " + str(SAMPLERATE))
print("Total number of frames: " + str(TOTALFRAMES))
print("Length: " + str(round(TOTALFRAMES/SAMPLERATE, 2)) + "s")
print("Sample width: " + str(SAMPLEWIDTH) + " bytes, or " + str(SAMPLEWIDTH*8) + " bits")
print("////////////////////////////////////////////////////////////////\n")

# Open the wave files we'll create to store the original audio file with different echoes
audioOut0 = wave.open("echo0.wav", "w")
audioOut0.setnchannels(2)
audioOut0.setsampwidth(2)
audioOut0.setframerate(44100)

audioOut1 = wave.open("echo1.wav", "w")
audioOut1.setnchannels(2)
audioOut1.setsampwidth(2)
audioOut1.setframerate(44100)

audioOut2 = wave.open("echo2.wav", "w")
audioOut2.setnchannels(2)
audioOut2.setsampwidth(2)
audioOut2.setframerate(44100)


# Get the raw audio from the wave file and convert it to an ndarray
signal = audio.readframes(-1)
signal = np.frombuffer(signal, "Int16", -1)

# Create a variable signalarray of type bytearray. This now contains the original audio
signalarray = bytearray(signal)

# Create a one second delay to place between echoes
zerosarray1sec = bytearray(BYTESINASEC)
#print(signalarray)

# Create some divisor bytearrays to create the echoes with
echodivisor0 = [4] * len(signal)

# Create some copies of the original audio with lower gain
#echoinstanceint0 = [int(v) for v in signalarray.split()]
#print(echoinstanceint0)
echoinstance0 = signal / echodivisor0
echoinstance0 = bytearray(echoinstance0)

# Create our echoed audio
signalOut0 = signalarray + zerosarray1sec
signalOut0[-1:-1] = echoinstance0
signalOut0 = np.frombuffer(signalOut0, "Int16", -1)
audioOut0.writeframes(signalOut0)


## Graphs

# The time variables for the horizontal axis of the audios
Time = np.linspace(0, len(signal)/SAMPLERATE, num=len(signal))

# Graph of original audio
plt.figure(1)
plt.title("Original Audio")
plt.plot(Time/NUMCHANNELS, signal/NUMCHANNELS)
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()

plt.figure(2)
plt.title("Echo 1")
plt.plot(np.frombuffer(signalarray, "Int16", -1))
plt.show()

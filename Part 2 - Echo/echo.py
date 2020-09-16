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
signal = np.frombuffer(signal, np.int16, -1)

# Create a variable signalarray of type bytearray. This now contains the original audio
signalarray = bytearray(signal)

# Create a one second delay to place between echoes
zerosarray1sec = bytearray(BYTESINASEC)
zerosarray1sec = np.frombuffer(zerosarray1sec, np.int16, -1)

signalOut = np.frombuffer(signalarray, np.int16, -1)

# Create some echoes of different amplitudes
echo0 = np.round(np.frombuffer(signalOut, np.int16, -1)*0.9)
echo0 = echo0.astype(np.int16)

echo1 = np.round(np.frombuffer(signalOut, np.int16, -1)*0.75)
echo1 = echo1.astype(np.int16)

echo2 = np.round(np.frombuffer(signalOut, np.int16, -1)*0.5)
echo2 = echo2.astype(np.int16)

# Creating the first audio file with echoes (1 echo)
audioOut0.writeframes(signalOut)
audioOut0.writeframes(zerosarray1sec)
audioOut0.writeframes(echo0)

# Creating the second audio file with echoes (2 echoes)
audioOut1.writeframes(signalOut)
audioOut1.writeframes(zerosarray1sec)
audioOut1.writeframes(echo0)
audioOut1.writeframes(zerosarray1sec)
audioOut1.writeframes(echo1)

# Creating the third audio file with echoes (3 echoes)
audioOut2.writeframes(signalOut)
audioOut2.writeframes(zerosarray1sec)
audioOut2.writeframes(echo0)
audioOut2.writeframes(zerosarray1sec)
audioOut2.writeframes(echo1)
audioOut2.writeframes(zerosarray1sec)
audioOut2.writeframes(echo2)

# Close all the audio streams
audioOut0.close()
audioOut1.close()
audioOut2.close()
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

# Graph of first echo file (1 echo)
audioGraph0 = wave.open("echo0.wav")
signalGraph0 = audioGraph0.readframes(-1)
signalGraph0 = np.frombuffer(signalGraph0, np.int16, -1)

plt.figure(2)
plt.title("Echo 1")
plt.plot(signalGraph0/NUMCHANNELS)
plt.show()

# Graph of second echo file (2 echoes)
audioGraph1 = wave.open("echo1.wav")
signalGraph1 = audioGraph1.readframes(-1)
signalGraph1 = np.frombuffer(signalGraph0, np.int16, -1)

plt.figure(3)
plt.title("Echo 2")
plt.plot(signalGraph1/NUMCHANNELS)
plt.show()

# Graph of the third echo file (3 echoes)
audioGraph2 = wave.open("echo2.wav")
signalGraph2 = audioGraph2.readframes(-1)
signalGraph2 = np.frombuffer(signalGraph2, np.int16, -1)

plt.figure(4)
plt.title("Echo 3")
plt.plot(signalGraph2/NUMCHANNELS)
plt.show()

# Title: EE 321 Project 1: Audio Manipulation. Part II: Echo
# Purpose: To implement echoes into a .wav audio file
# Developers: Cameron Palmer, Shawn Boyd, Siddesh Sood
# Last Modified: September 17, 2020

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

# Open the wave files we'll create to store the original audio file with different reverberations
audioOut0 = wave.open("reverb0.wav", "w")
audioOut0.setnchannels(2)
audioOut0.setsampwidth(2)
audioOut0.setframerate(44100)

audioOut1 = wave.open("reverb1.wav", "w")
audioOut1.setnchannels(2)
audioOut1.setsampwidth(2)
audioOut1.setframerate(44100)

audioOut2 = wave.open("reverb2.wav", "w")
audioOut2.setnchannels(2)
audioOut2.setsampwidth(2)
audioOut2.setframerate(44100)

# Get the raw audio from the wave file and convert it to an ndarray
signal = audio.readframes(-1)
signal = np.frombuffer(signal, np.int16, -1)

# Create a variable signalarray of type bytearray. This now contains the original audio
signalarray = bytearray(signal)

# Convert signalarray back into an ndarray to be able to write it out
signalOut = np.frombuffer(signalarray, np.int16, -1)

# Create some echoes of different amplitudes
echo0 = np.round(np.frombuffer(signalOut, np.int16, -1)*0.9)
echo0 = echo0.astype(np.int16)

echo1 = np.round(np.frombuffer(signalOut, np.int16, -1)*0.75)
echo1 = echo1.astype(np.int16)

echo2 = np.round(np.frombuffer(signalOut, np.int16, -1)*0.5)
echo2 = echo2.astype(np.int16)

# Create a constant to standardize how much the reverberations overlap
AMOUNTTOREVERB = 100000

# Creating the first audio file with reverberations (1 reverberation) #
signalOut0 = signalOut[0:len(signalOut)-AMOUNTTOREVERB-1]  # Create the non-overlapped part of the signal
signalOut0 = np.append(signalOut0, np.add(signalOut[len(signalOut)-AMOUNTTOREVERB-1:-1], echo0[0:AMOUNTTOREVERB]))  # Add in the overlapped part of the signal
signalOut0 = np.append(signalOut0, echo0[AMOUNTTOREVERB:-1])  # Finish with the non-overlapped end of the echo

audioOut0.writeframes(signalOut0)

# Creating the second audio file with reverberations (2 reverberations)
signalOut1 = signalOut0[0:len(signalOut0)-AMOUNTTOREVERB-1]  # Start with the previous reverberated signal
signalOut1 = np.append(signalOut1, np.add(signalOut0[len(signalOut0)-AMOUNTTOREVERB-1:-1], echo1[0:AMOUNTTOREVERB]))
signalOut1 = np.append(signalOut1, echo1[AMOUNTTOREVERB:-1])

audioOut1.writeframes(signalOut1)

# Creating the third audio file with reverberations
signalOut2 = signalOut1[0:len(signalOut1)-AMOUNTTOREVERB-1]
signalOut2 = np.append(signalOut2, np.add(signalOut1[len(signalOut1)-AMOUNTTOREVERB-1:-1], echo2[0:AMOUNTTOREVERB]))
signalOut2 = np.append(signalOut2, echo2[AMOUNTTOREVERB:-1])

audioOut2.writeframes(signalOut2)

# Close all the audio streams
audioOut0.close()
audioOut1.close()
audioOut2.close()

## Graphs
# Graph of original audio
Time = np.linspace(0, len(signal)/SAMPLERATE, num=len(signal))  # For horizontal axis
plt.figure(1)
plt.title("Original Audio")
plt.plot(Time/NUMCHANNELS, signal/NUMCHANNELS)
plt.xlabel("Time (s)")
plt.ylabel("Value")

# Graph of first echo file (1 echo)
audioGraph0 = wave.open("reverb0.wav")
signalGraph0 = audioGraph0.readframes(-1)
signalGraph0 = np.frombuffer(signalGraph0, np.int16, -1)

Time0 = np.linspace(0, len(signalGraph0)/SAMPLERATE, num=len(signalGraph0))  # For horizontal axis
plt.figure(2)
plt.title("Reverberation 1")
plt.plot(Time0/NUMCHANNELS, signalGraph0/NUMCHANNELS)
plt.xlabel("Time (s)")
plt.ylabel("Value")

# Graph of second echo file (2 echoes)
audioGraph1 = wave.open("reverb1.wav")
signalGraph1 = audioGraph1.readframes(-1)
signalGraph1 = np.frombuffer(signalGraph1, np.int16, -1)

Time1 = np.linspace(0, len(signalGraph1)/SAMPLERATE, num=len(signalGraph1))  # For horizontal axis
plt.figure(3)
plt.title("Reverberation 2")
plt.plot(Time1/NUMCHANNELS, signalGraph1/NUMCHANNELS)
plt.xlabel("Time (s)")
plt.ylabel("Value")

# Graph of the third echo file (3 echoes)
audioGraph2 = wave.open("reverb2.wav")
signalGraph2 = audioGraph2.readframes(-1)
signalGraph2 = np.frombuffer(signalGraph2, np.int16, -1)

Time2 = np.linspace(0, len(signalGraph2)/SAMPLERATE, num=len(signalGraph2))  # For horizontal axis
plt.figure(4)
plt.title("Reverberation 3")
plt.plot(Time2/NUMCHANNELS, signalGraph2/NUMCHANNELS)
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()

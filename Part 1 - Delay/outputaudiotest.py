import matplotlib.pyplot as plt
import numpy as np
import wave
from playsound import playsound as ps

audio = wave.open("delay1.wav")

# Print out some basic information about the audio file
print("\n//////////////////Info for original audio file//////////////////")
print("Number of channels (1 for mono, 2 for stereo): " + str(audio.getnchannels()))
print("Sample rate: " + str(audio.getframerate()))
print("Total number of frames: " + str(audio.getnframes()))
print("Length: " + str(round(audio.getnframes()/audio.getframerate(), 2)) + "s")
print("Sample width: " + str(audio.getsampwidth()) + " bytes, or " + str(audio.getsampwidth()*8) + " bits")
print("////////////////////////////////////////////////////////////////\n")


ps("delay3.wav")

import wave
import matplotlib.pyplot as plt
import numpy as np

# Import audio file as wave object
audio_to_compare = wave.open("./audios_compare/3seat_adicao_01.wav", "r") # audio que busco melhor aproximação do original_audio
original_audio = wave.open("audios_compare/seat_gtts.wav", "r") # audio do gtts

# Convert wave object to bytes
soundwave_to_compare = audio_to_compare.readframes(-1)
soundwave_original = original_audio.readframes(-1)

# View the wav file in byte form print(soundwave_audio_to_compare)
# Convert soundwave_gm from bytes to integers
signal_to_compare = np.frombuffer(soundwave_to_compare, dtype='int16')
signal_original = np.frombuffer(soundwave_original, dtype='int16')

framerate_to_compare = audio_to_compare.getframerate()
time_to_compare = np.linspace(start=0,
                              stop=len(signal_to_compare) / framerate_to_compare,
                              num=len(signal_to_compare))

framerate_original = original_audio.getframerate()
time_original = np.linspace(start=0,
                              stop=len(signal_original) / framerate_original,
                              num=len(signal_original))

# Initialize figure and setup title
plt.title("Good Afternoon vs. Good Morning")
# x and y axis labels
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
# Add good morning and good afternoon values
plt.plot(time_to_compare, signal_to_compare, label="Good Afternoon")
plt.plot(time_original, signal_original, label="Good Morning", alpha=0.5)

# Create a legend and show our plot
plt.legend()
plt.show()

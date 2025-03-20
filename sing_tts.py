import librosa
import soundfile as sf
import numpy as np


# Step 2: Load the Speech Audio
y, sr = librosa.load(r"C:\Users\bigny\OneDrive\Desktop\tamul-ai\frontend\src\assets\female_b25cc826-2b3b-47a8-9158-20a9a8fe944e.wav", sr=None)

# Step 3: Slow Down the Speech to a Singing Tempo
y_slow = librosa.effects.time_stretch(y, rate=0.7)  # 0.7 makes it slower

# Step 4: Apply Pitch Shifting to Make it Sound More Musical
y_slow_pitch = librosa.effects.pitch_shift(y_slow, sr=sr, n_steps=4) 

# Step 5: Add Vibrato Effect for a Singing Feel
vibrato = np.sin(2 * np.pi * np.arange(len(y_slow_pitch)) * 5 / sr) * 0.01
y_singing = y_slow_pitch + vibrato  # Apply vibrato to the voice

# Step 6: Save the Final Singing Audio
sf.write("singing_output.mp3", y_singing, sr)

print("Singing voice generated and saved as singing_output.mp3 🎶")

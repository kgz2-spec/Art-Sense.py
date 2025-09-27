import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog  
import numpy as np

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Load painting
img = io.imread("starry night.jpeg")
pixels = img.reshape(-1, 3)

# Get average color
avg_color = np.mean(pixels, axis=0)
print("Average RGB:", avg_color)

# Simple rule-based "emotion inference"
r, g, b = avg_color
if r > g and r > b:
    mood = "Energetic / Passionate"
elif b > r and b > g:
    mood = "Calm / Melancholic"
elif g > r and g > b:
    mood = "Natural / Peaceful"
else:
    mood = "Neutral / Balanced"

print("Inferred mood from colors:", mood)

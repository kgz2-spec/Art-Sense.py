import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog  
import numpy as np

import cv2
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

def get_dominant_color(image, k=3):
    """Find dominant color in BGR image using k-means clustering."""
    data = image.reshape((-1, 3))
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    counts = Counter(labels.flatten())
    dominant = centers[counts.most_common(1)[0][0]]
    return dominant[::-1]  # convert BGR → RGB

def analyze_emotion(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize for consistency
    img_small = cv2.resize(img, (256, 256))

    # 1. Color analysis
    dom_color = get_dominant_color(img_small, k=3)
    r, g, b = dom_color

    # 2. Edge density (measure of "chaos")
    gray = cv2.cvtColor(img_small, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.sum(edges) / edges.size

    # Simple rule-based emotion mapping
    emotion = "neutral"
    if r > 150 and r > g and r > b:
        emotion = "angry / passionate"
    elif b > 150 and b > r and b > g:
        emotion = "sad / calm"
    elif g > 150 and g > r and g > b:
        emotion = "peaceful / natural"
    elif (r + g) / 2 > 150 and b < 100:
        emotion = "happy / energetic"

    if edge_density > 50:  # high chaos
        emotion += " + anxious/tense"

    # Show image + edges
    plt.subplot(1, 2, 1)
    plt.imshow(img_small)
    plt.title("Drawing")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap="gray")
    plt.title("Edges (chaos measure)")
    plt.axis("off")

    plt.show()

    return {
        "dominant_color": dom_color,
        "edge_density": edge_density,
        "inferred_emotion": emotion
    }

# Example usage:
result = analyze_emotion("your_drawing.png")
print(result)


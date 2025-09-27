import cv2
import matplotlib.pyplot as plt
import os # Import the os module for path checking
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def display_image(image_path):
    """
    Reads an image from the given path, displays it using Matplotlib,
    and saves it as 'output_image.jpg'.
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from {image_path}. Please check the path and file type.")
        return

    # Convert the image from BGR to RGB format for Matplotlib display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the image using Matplotlib
    plt.imshow(image_rgb)
    plt.title(f"Displayed Image: {os.path.basename(image_path)}")
    plt.axis('off')  # Hide axis
    plt.show()

    # Save the original image using OpenCV
    output_filename = 'output_image.jpg'
    cv2.imwrite(output_filename, image)
    print(f"Image saved as '{output_filename}'")
    print("Image displayed successfully.")

def main():
    """
    Main function to ask the user for an image path and process it.
    """
    while True:
        user_input_path = input("Please enter the path to your image file (e.g., my_image.jpg or C:/Users/Me/Pictures/image.png): ")

        # Basic validation: check if the file exists
        if not os.path.exists(user_input_path):
            print(f"Error: The file '{user_input_path}' does not exist. Please try again.")
            continue
        elif not os.path.isfile(user_input_path):
            print(f"Error: The path '{user_input_path}' is not a file. Please try again.")
            continue
        else:
            # If the path is valid, try to display and save the image
            display_image(user_input_path)
            break # Exit the loop after processing
def browse_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    if file_path:
        # Open and display the selected image
        img = Image.open(file_path)
        img = img.resize((300, 300))  # Resize image to fit the window
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    # Ensure you have the necessary libraries installed:
    # pip install opencv-python matplotlib
    main()

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Add a button to browse for an image
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack(pady=10)

# Add a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Run the Tkinter event loop
root.mainloop()

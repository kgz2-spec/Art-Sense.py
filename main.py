import cv2
import matplotlib.pyplot as plt
import os # Import the os module for path checking
import tkinter as tk

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

if __name__ == "__main__":
    # Ensure you have the necessary libraries installed:
    # pip install opencv-python matplotlib
    main()

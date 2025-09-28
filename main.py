import requests
import google.generativeai as genai
from io import BytesIO

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyCrBT3cWKWwtFhcuzArJBupI_-x92qP_KI") 

# Function to download image and return bytes
def get_image_bytes_from_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BytesIO(response.content)

# Function to send image and prompt to Gemini
def gemini_call(image_url):
    image_bytes = get_image_bytes_from_url(image_url)

    model = genai.GenerativeModel("gemini-2.5-flash") 

    # Prompt for image analysis
    prompt = (
        "Please analyze this image based on the following criteria:\n"
        "- Color palette\n"
        "- Shapes and forms\n"
        "- Composition (rule of thirds, balance, etc.)\n"
        "- Shading and lighting\n"
        "- Linework (thickness, style, direction)\n"
        "- General description of the image/artwork"
    )

    # Generate content using image + prompt
    response = model.generate_content([image_bytes, prompt])

    return response.text

# Get URL from user
def get_image_url():
    return input("Please enter the URL of the image you want analyzed: ")

# Main logic
def main():
    image_url = get_image_url()
    if image_url:
        try:
            result = gemini_call(image_url)
            print("\n🔍 Image Analysis Result:\n")
            print(result)
        except Exception as e:
            print("❌ Error analyzing image:", e)
    else:
        print("⚠️ No URL provided.")

if __name__ == "__main__":
    main()

'''
import requests
from google import genai
import google.generativeai as genai
from PIL import Image
from io import BytesIO

def get_image_bytes_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise error if download fails
    return BytesIO(response.content)

def gemini_call(image_url):
    image_bytes = get_image_bytes_from_url(image_url)
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client(api_key="AIzaSyCrBT3cWKWwtFhcuzArJBupI_-x92qP_KI")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"Based on {image_bytes}, analyze its color, shape, composition, shading/Lighting, linework (thickness), and create a general summary on the artwork or image."
    )
    return(response.text)

# Save the image locally
def get_image_url():
    image_url = input("Please enter your image url: ")
    #Download the image
    return image_url

# Function to send the image to Gemini API and get analysis
def analyze_image():
    analysis = gemini_call(get_image_url())
    return analysis

# Main function to handle the process
def main():
    image_data = get_image_url()
    if image_data:
        analysis_result = analyze_image()
        if analysis_result:
            print("Image Analysis Result:")
            print(analysis_result)
        else:
            print("Failed to analyze the image.")
    else:
        print("No image data provided.")

if __name__ == "__main__":
    main()
'''
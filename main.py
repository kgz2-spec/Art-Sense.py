
import requests
import google.generativeai as genai
from io import BytesIO
from PIL import Image

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
    genai.configure(api_key="AIzaSyCrBT3cWKWwtFhcuzArJBupI_-x92qP_KI")
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
    image = Image.open(image_bytes)
    response = model.generate_content([image, prompt])

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

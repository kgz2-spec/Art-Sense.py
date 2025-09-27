import requests

# Function to prompt user for an image file
def get_image_file():
    file_path = input("Please provide the path to your image file: ")
    try:
        with open(file_path, 'rb') as image_file:
            return image_file.read()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None

# Function to send the image to Gemini API and get analysis
def analyze_image(image_data):
    api_url = "https://api.gemini.google.dev/analyze"  
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/octet-stream"
    }
    try:
        response = requests.post(api_url, headers=headers, data=image_data)
        response.raise_for_status()
        return response.json()  # Assuming the API returns JSON
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None

# Main function to handle the process
def main():
    image_data = get_image_file()
    if image_data:
        analysis_result = analyze_image(image_data)
        if analysis_result:
            print("Image Analysis Result:")
            print(analysis_result)
        else:
            print("Failed to analyze the image.")
    else:
        print("No image data provided.")

if __name__ == "__main__":
    main()
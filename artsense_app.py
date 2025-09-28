from flask import Flask, render_template, request, jsonify
from main import gemini_call  # Import analysis function
import threading
import webbrowser

app = Flask("ArtSense")

@app.route('/')
def index():
    return render_template('girlhacks.html')  # Serve frontend

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    image_url = data.get('url')

    if not image_url:
        return jsonify({'error': 'No image URL provided'}), 400

    try:
        result = gemini_call(image_url)  # Call analysis logic
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#  Function to open browser after server starts
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    #  Launch browser in separate thread so it doesn’t block the server
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)

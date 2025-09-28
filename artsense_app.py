from flask import Flask, render_template, request, jsonify
from main import gemini_call  # Import analysis function

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

if __name__ == '__main__':
    app.run(debug=True)
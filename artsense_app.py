from flask import Flask, render_template, request, jsonify
from main import gemini_call  # Import analysis function
from flask import Flask, render_template, request, jsonify
from main import gemini_call  # Import analysis function
import os
import sys

app = Flask(__name__)


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


def main():
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') in ('1', 'true', 'True')

    try:
        app.run(host=host, port=port, debug=debug)
    except OSError as e:
        if e.errno == 48 or 'Address already in use' in str(e):
            print(f"Port {port} is already in use.\n" \
                  f"Either stop the process that is using the port or run with a different port, e.g.\\n" \
                  f"  export PORT=5001 && python {os.path.basename(sys.argv[0])}" , file=sys.stderr)
            sys.exit(1)
        else:
            raise


if __name__ == '__main__':
    main()
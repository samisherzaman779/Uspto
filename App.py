from flask import Flask, request, jsonify
from Main_Scraper import run_scraper

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the USPTO Scraper API!",
        "usage": "Upload a .txt file to /scrape-file using form-data"
    })

@app.route('/scrape-file', methods=['POST'])
def scrape_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file.filename is None or not file.filename.endswith('.txt'):
        return jsonify({"error": "Only .txt files are allowed"}), 400

    try:
        # Read uploaded file
        content = file.read().decode('utf-8')
        urls = [line.strip() for line in content.splitlines() if line.strip()]
        
        if not urls:
            return jsonify({"error": "No valid URLs found in the file"}), 400

        results = run_scraper(urls)

        return jsonify({
            "message": "✅ Scraping completed successfully",
            "count": len(results),
            "processed_urls": results
        })
    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

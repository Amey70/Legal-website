from flask import Flask, request, jsonify
from flask_cors import CORS

from extractor import extract_text
from summarizer import generate_summary, translate_text

app = Flask(__name__)
CORS(app)

@app.route("/api/analyze", methods=["POST"])
def analyze_document():

    try:
        file = request.files["file"]
        language = request.form.get("language")

        # Step 1 Extract text
        text = extract_text(file)

        if len(text.strip()) == 0:
            return jsonify({"success": False, "error": "No text found"})


        # Step 2 Summarize
        summary = generate_summary(text)


        # Step 3 Translate
        translated_summary = translate_text(summary, language)

        return jsonify({
            "success": True,
            "summary": translated_summary
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/")
def home():
    return "LexPopuli AI Backend Running"
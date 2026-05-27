import pdfplumber
import docx
import pytesseract
from PIL import Image
import io

def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    elif filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif filename.endswith((".png",".jpg",".jpeg")):
        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)
        return text

    else:
        return ""
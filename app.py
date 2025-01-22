from flask import Flask, request, jsonify
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
import pytesseract
from io import BytesIO

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        # Check if the file key is in the request
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})

        image_file = request.files['image']

        # Load the image using PIL
        image = Image.open(image_file)
         # Convert the image to grayscale
        grayscale_image = ImageOps.grayscale(image)
        #   # Invert the grayscale image if needed
        # inverted_image = ImageOps.invert(grayscale_image)
        # enhanced_image = ImageEnhance.Contrast(grayscale_image).enhance(2.5)
        
        # denoised_image = enhanced_image.filter(ImageFilter.MedianFilter)
        # custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/`~"\' -c tessedit_unrej_any=1 -c tessedit_write_images=true'
        # text = pytesseract.image_to_string(enhanced_image)
        text = pytesseract.image_to_string(grayscale_image)
        # text = pytesseract.image_to_string(image)
        
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': f'Error predicting text: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)

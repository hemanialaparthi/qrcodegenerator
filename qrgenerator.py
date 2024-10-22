from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form.get('link')  # Get the link from the form

    if data:  # Check if data is provided
        memory = BytesIO()
        img = qrcode.make(data)  # Generate the QR code
        img.save(memory, format='PNG')  # Save to BytesIO as PNG
        memory.seek(0)

        # Encode the image in base64
        base64_img = base64.b64encode(memory.getvalue()).decode('utf-8')
        img_tag = f"data:image/png;base64,{base64_img}"

        return render_template('index.html', qr_code=img_tag)  # Pass the QR code image to the template

    return render_template('index.html', error="Please provide a valid link.")


if __name__ == '__main__':
    app.run(debug=True)

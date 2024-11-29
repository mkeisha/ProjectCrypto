import os
from flask import Flask, request, render_template, send_file
from encryption import encrypt_file
from decryption import decrypt_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Encrypt the file
        encrypted_filepath = encrypt_file(filepath, app.config['DOWNLOAD_FOLDER'])

        return render_template('result.html', file_path=encrypted_filepath, action='Encrypted')
    return "File upload failed!"

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Decrypt the file
        decrypted_filepath = decrypt_file(filepath, app.config['DOWNLOAD_FOLDER'])

        return render_template('result.html', file_path=decrypted_filepath, action='Decrypted')
    return "File upload failed!"

if __name__ == '__main__':
    app.run(debug=True)

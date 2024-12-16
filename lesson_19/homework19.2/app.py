import os
from flask import Flask, request, jsonify, send_file, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    print(f'Saving file to: {file_path}')
    file.save(file_path)
    return jsonify({'image_url': f'http://127.0.0.1:8080/uploads/{file.filename}'}), 201


@app.route('/image/<filename>', methods=['GET'])
def get_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    if request.headers.get('Content-Type') == 'text':
        return jsonify({'image_url': f'http://127.0.0.1:8080/uploads/{filename}'})
    return send_file(file_path)


@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True, port=8080)

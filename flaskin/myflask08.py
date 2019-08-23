#!/usr/bin/python3

from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = '/home/student/pyapivz/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        #f.save(os.path.join['UPLOAD_FOLDER'], filename)
        return 'File successfully uploaded!'

if __name__ == '__main__':
    app.run(port=5006)

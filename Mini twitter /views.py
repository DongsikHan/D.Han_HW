from flask import render_template, request, url_for, redirect
from apps import app

from google.appengine.ext import db


class Photo(db.Model):
    photo = db.BlobProperty()
    txt = db.StringProperty()
    time_prop = db.DateTimeProperty(auto_now=True)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    q = Photo.all()
    q.order('-time_prop')
    return render_template("upload.html", all_list=q)


@app.route('/upload', methods=['POST'])
def upload_db():
    post_data = request.files['photo']
    post_txt = request.form['words']

    if post_data and allowed_file(post_data.filename):
        filestream = post_data.read()
        filestream2 = post_txt

        upload_data = Photo()
        upload_data.photo = db.Blob(filestream)
        upload_data.txt = filestream2
        got = upload_data.put()

        comment = "uploaded!"

    else:
        comment = "please upload valid image file"

    return redirect(url_for('index'))


@app.route('/show/<key>')
def shows(key):
    uploaded_data = db.get(key)
    return app.response_class(uploaded_data.photo)

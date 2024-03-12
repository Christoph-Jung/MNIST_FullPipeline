import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename

import config

app = Flask(__name__)
app.config.from_object(config.Config)


class UploadFile(FlaskForm):
    file_upload = FileField("File", validators=[InputRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField("Upload File")


@app.route('/')
@app.route('/home/')
def home():
    return "Testing <b>home</b> route..."


@app.route('/users/<name>')
def user(name: str) -> str:
    return (f"The user has the name: {name}.")


@app.route('/model/', methods=['GET', 'POST'])
def model():
    form = UploadFile()
    if form.validate_on_submit():
        file = form.file_upload.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        filename = "placeholder.png"
    print(f"Current image path: {filename}")
    return render_template('index.html', form=form, image_path=filename)


def main():
    app.run(host="0.0.0.0", port=5001, debug=True)


if __name__ == '__main__':
    main()

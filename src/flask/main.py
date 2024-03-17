import os
import sys
from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename


import config
from .. import models as models

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


print(f"Current working dir: {os.getcwd()}")
CURRENT_MODEL = models.svm.MnistSvm()

app = Flask(__name__)
app.config.from_object(config.Config)
MODELS = ["SVM", "CNN", "Bayes"]
MODEL_INDEX = 0
CLASSIFYING_RESULT = "STUFF"


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
    tmp_models = MODELS.copy()
    tmp_models.remove(tmp_models[MODEL_INDEX])
    print(f"Current model: {MODELS[MODEL_INDEX]}")
    print(f"Rest: {tmp_models}")
    return render_template('index.html',
                           form=form,
                           image_path=filename,
                           models=tmp_models,
                           current_model=MODELS[MODEL_INDEX],
                           result=CLASSIFYING_RESULT)


@app.route('/dropdown', methods=['POST'])
def drop():
    global MODEL_INDEX
    dropdownval = request.form.get('Models')
    MODEL_INDEX = MODELS.index(dropdownval)
    print(dropdownval)
    print(CURRENT_MODEL.print_stuff())
    return redirect("/model", code=302)


def main():
    app.run(host="0.0.0.0", port=5001, debug=True)


if __name__ == '__main__':
    main()

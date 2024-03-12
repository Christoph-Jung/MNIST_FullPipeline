import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'securePass'
    UPLOAD_FOLDER = 'src/flask/static'
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000     # 16 megabytes

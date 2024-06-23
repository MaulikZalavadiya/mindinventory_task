import os

class Config:
    MONGO_URI = 'mongodb://localhost:27017'
    UPLOAD_FOLDER = 'media'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

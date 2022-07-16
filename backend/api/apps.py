from django.apps import AppConfig
from cv2 import VideoCapture


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    web_cam = VideoCapture(1)

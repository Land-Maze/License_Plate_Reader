# Create your views here.

from django.http import StreamingHttpResponse, HttpResponseServerError
from api.apps import ApiConfig
from cv2 import VideoCapture, cvtColor, COLOR_BGR2GRAY, flip, imencode

def gen(camera = VideoCapture(0)):
    while True:
        res, frame = camera.read()
        frame = cvtColor(frame, COLOR_BGR2GRAY)
        frame = flip(frame, 1)
        frame = imencode('.jpeg', frame)[1].tobytes()
        
        if not res:
            return HttpResponseServerError()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	return StreamingHttpResponse(
                                gen(ApiConfig.web_cam), 
                                content_type='multipart/x-mixed-replace; boundary=frame'
                                )

def license_plate(request):
    return HttpResponseServerError({'error': 'Not implemented'})
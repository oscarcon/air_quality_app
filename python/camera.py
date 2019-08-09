import cv2
import numpy as np
from time import sleep
from time import time
#video = cv2.VideoCapture('rtsp://admin:dvt@12345@192.168.1.164:554/Streaming/Channels/101')
from PIL import Image
import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from io import BytesIO
import threading
from queue import Queue

share_queue = Queue(maxsize=1)
#url = 'http://192.168.1.164/ISAPI/Streaming/Channels/101/Picture'
#response = requests.get(url, auth=HTTPDigestAuth('admin', 'dvt@12345'))
#url = 1
url = 'rtsp://192.168.1.28:8080/h264_ulaw.sdp'
video = cv2.VideoCapture(url)
#image = np.array([])
def get_frame(share_queue):
    while True:
        ret, image = video.read()
        with share_queue.mutex:
        	share_queue.queue.clear()
        share_queue.put_nowait(image)

threading.Thread(target=get_frame, args=(share_queue,)).start()

while True:
    #ret, frame = video.read()
    #response = requests.get(url)
    #img = Image.open(BytesIO(response.content))
    #frame = cv2.resize(frame, (1024,768))
   # frame = np.array(img)
    cv2.imshow('frame', share_queue.get())
    cv2.waitKey(1)
    #qprint(time())
    # sleep(0.1)
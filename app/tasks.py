''' Tasks related to our celery functions '''

import time
import random
import datetime

from io import BytesIO
from celery import Celery, current_task
from celery.result import AsyncResult

from PIL import Image  
import os
import time

REDIS_URL = 'redis://redis:6379/0'
BROKER_URL = 'amqp://admin:mypass@rabbit//'

CELERY = Celery('tasks',
                backend=REDIS_URL,
                broker=BROKER_URL)

CELERY.conf.accept_content = ['json', 'msgpack']
CELERY.conf.result_serializer = 'msgpack'

def get_job(job_id):
    '''
    To be called from our web app.
    The job ID is passed and the celery job is returned.
    '''
    return AsyncResult(job_id, app=CELERY)

@CELERY.task()
def image_demension(img):
    time.sleep(2)
    im = Image.open(img)  
    width, height = im.size  
    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5

    # Cropped image of above dimension  \
    im1 = im.crop((left, top, right, bottom)) 
    newsize = (300, 300) 
    im1 = im1.resize(newsize) 
    width, height = im1.size  
    location=os.path.join('static/worker-img','cropped_img.'+im.format.lower())
    im1.save(os.path.join('static/worker-img','cropped_img.'+im.format.lower()))   
    print(width,height)
    print("pass")

    return location

# import the necessary packages
import numpy as np
import time
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from sauron import look_left, look_straight, look_right
from sense_hat import SenseHat

# initialize the camera and grab a reference to the raw camera capture
sense = SenseHat()
sleep = 0.2
res1 = 400
res2 = 400
camera = PiCamera()
camera.rotation = 180
camera.resolution = (res1, res2)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(res1, res2))

left1 = look_left(1)
right1 = look_right(1)
straight1 = look_straight(1)

found_face = False
no_face_count = 0

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('data/deploy.prototxt.txt', 'data/res10_300x300_ssd_iter_140000.caffemodel')

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] starting video stream...")
time.sleep(1.0)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    frame = frame.array
    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))
 
    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()
    # loop over the detections
    # If there was no face detected in previous frame, go to centre
    # If there was a face than pevious direction will be kept
    if round(no_face_count/detections.shape[2]) > 5:
        sense.set_pixels(straight1)
        time.sleep(sleep)
    
    # Now loop over the detections
    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        print(i)
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence < 0.951:
            no_face_count += 1
            #print('no face detected',i)
            direction = 'straight'
            continue
        
        else:
            found_face = True
            no_face_count = 0
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
           # draw the bounding box of the face along with the associated
            # probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
#             cv2.rectangle(frame, (startX, startY), (endX, endY),
#                 (0, 0, 255), 2)
        
            if startX >= 200 and startX <= 400:
                direction = 'left'
                sense.set_pixels(left1)
                print('I see you....',i)
        
            elif startX >= 0 and startX <= 199:
                direction = 'right'
                sense.set_pixels(right1)
                print('I see you....',i)
            else:
                direction = 'straight'
                sense.set_pixels(straight1)

            time.sleep(sleep)

        print(direction,confidence)
        
    # show the output frame
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()

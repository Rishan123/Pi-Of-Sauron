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
upper_red = [0, 0, 255]
lower_red = [0, 0, 255]
upper_red = np.array(upper_red)
lower_red = np.array(lower_red)

left1 = look_left(1)
left2 = look_left(2)
left3 = look_left(3)

right1 = look_right(1)
right2 = look_right(2)
right3 = look_right(3)

straight1 = look_straight(1)
straight2 = look_straight(2)
straight3 = look_straight(3)

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
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence < 0.951:
            found_face = True
            continue

        # compute the (x, y)-coordinates of the bounding box for the
        # object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
         
        # draw the bounding box of the face along with the associated
        # probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
            (0, 0, 255), 2)
    
        if startX >= 200 and startX <= 400:
            direction = 'right'
            sense.set_pixels(right1)
            time.sleep(sleep)
            print('I see you....')
            time.sleep(sleep*10)
            sense.set_pixels(straight1)

        elif startX >= 0 and startX <= 199:
            direction = 'left'
            sense.set_pixels(left1)
            time.sleep(sleep)
            print('I see you....')
            time.sleep(sleep*10)
            sense.set_pixels(straight1)
        
        print(direction)
        
    # show the output frame
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
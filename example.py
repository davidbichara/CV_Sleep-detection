"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import time
import win32api 
import random as rnd

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
clock = 0
end = 0


while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking() and clock == 0:
        text = "Blinking " 
        clock = time.time()
        end = 0
    elif gaze.is_blinking() and clock != 0:
        text = "Blinking " 
        end = time.time()
    elif gaze.is_right():
        text = "Looking right"
        clock = 0
        end = 0
    elif gaze.is_left():
        text = "Looking left"
        clock = 0
        end = 0
    elif gaze.is_center():
        text = "Looking center"
        clock = 0
        end = 0

    if clock-end > 1:
        #for i in range(5):
        win32api.Beep(rnd.randint(37,10000), rnd.randint(750,3000))
        
    
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.namedWindow("Demo", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow("Demo", frame)
    cv2.setWindowProperty("Demo",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()

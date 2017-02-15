# Import the required modules
import dlib
import cv2
import argparse as ap
import get_points
import simplerename
import os
import shutil
def dl(source=0, dispLoc=False):
    cam = cv2.VideoCapture(source)
    print("cam:",cam);    
    print(cam.isOpened());
 
    if not cam.isOpened():
        return;
    
    while True:
        retval, img = cam.read()
        if not retval:
            exit()
        if(cv2.waitKey(25)==ord('p')):
            break	
        cv2.namedWindow("Object Tracking", cv2.WINDOW_NORMAL)
        cv2.imshow("Object Tracking", img)

    cv2.destroyWindow("Object Tracking")
    points = get_points.run(img) 

    if not points:
        while(true):
		sleep(1);
		points=get_points.run(img);
		print points;
		if  points:
			break;
		   
    
    cv2.namedWindow("Object Tracking", cv2.WINDOW_NORMAL)
    cv2.imshow("Object Tracking", img)
    tracker = dlib.correlation_tracker()
    tracker.start_track(img, dlib.rectangle(*points[0]))

    while True:
        retval, img = cam.read()	
        if not retval:
	    cam.release()
	    cv2.destroyAllWindows()
            exit()
        tracker.update(img)
        rect = tracker.get_position()
        pt1 = (int(rect.left()), int(rect.top()))
        pt2 = (int(rect.right()), int(rect.bottom()))
        cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
        if dispLoc:
            loc = (int(rect.left()), int(rect.top()-20))
            txt = "Object tracked at [{}, {}]".format(pt1, pt2)
            cv2.putText(img, txt, loc , cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
        cv2.namedWindow("Object Tracking", cv2.WINDOW_NORMAL)
        cv2.imshow("Object Tracking", img)
	key = cv2.waitKey(1) & 0xFF
        if key==ord("b"):
		cam.release()
		cv2.destroyAllWindows()
                break
    cam.release()

import os,random,string,shutil
import datetime 
import numpy as np
import datetime
import argparse
import Image
import cv2
import dltracker
import dlib
import cv2
import argparse as ap
import get_points
import simplerename
import os
import shutil

frame = None
roiPts = []
inputMode = False

def selectROI(event, x, y, flags, param):
	global frame, roiPts, inputMode
	if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
		roiPts.append((x, y))
		cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
		cv2.imshow("Object Traking", frame)

def cv(source,model):
	global frame, roiPts, inputMode
	camera = cv2.VideoCapture(source)
	if not camera.isOpened():
		camera=cv2.VideoCapture(0);
	cv2.namedWindow("Object Traking")
	cv2.setMouseCallback("Object Traking", selectROI)

	termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
	roiBox = None

	while True:	
		(grabbed, frame) = camera.read()
		if not grabbed:
			break
		if roiBox is not None:
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)
			(r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
			pts = np.int0(cv2.boxPoints(r))
			cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
		cv2.imshow("Object Traking", frame)
		key = cv2.waitKey(25) & 0xFF
		if key == ord("i") and len(roiPts) < 4:
			inputMode = True
			orig = frame.copy()
			img=Image.open(model);
			xsize,ysize=img.size;
			img=np.asarray(img);
			roi=img;
			
			roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
			roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
			roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
		
			roiBox = (0,0, xsize,ysize)
			print xsize,ysize
		elif key == ord("b"):
			camera.release()
			break
	camera.release()
	cv2.destroyAllWindows()

def getTimeName():	

	    	i=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
		name="{0}.png".format(i);
		return name;

def saveImage(roi,filename):
		if(filename<=0):
			filename=getTimeName();
		im=Image.fromarray(roi);
		im.save("images/"+filename);

if __name__ == "__main__":
	
    print "please input i to start track the object or choose the object, and input b to back."
    while(True):
            menu=raw_input("input 'g' use cam or 'h' use video , q to quit :");
	    if(menu=="g"):
		source=raw_input("please input the cam id:");
		isource=int(source);
		model="model/demo.png";
		m=raw_input("input 'g' to use default model or 'h'use draw box input b to bark:");
		if(m=="g"):		   
	            cv(isource,model);	
		elif(m=="h"):
		    dltracker.dl(isource,dispLoc=True);
	    elif(menu=="h"):
		source=raw_input("please input the video file path :")
		m=raw_input("input 'g' to use default model or 'h'use draw box. input b to bark:");  	
		model="model/man.png";
		if(m=="g"):
	            cv(source,model);	
		elif(m=="h"):
		    dltracker.dl(source,dispLoc=True); 	 
	    elif(menu=="q"):
		exit();   	    
	        
	    

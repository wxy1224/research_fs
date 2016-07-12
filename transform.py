#!/usr/bin/env python
 
import cv2
import numpy as np
 
def run(i) :
 
    # Read source image.
    im_src = cv2.imread('2014CarolinaKostnerFS3cut/frame%d.jpg' % i )
    # Four corners of the book in source image
    #pts_src = np.array([[float(99),float(-70)], [float(17),float(521)], [float(103),float(792)],[float(321),float(68)]])
    pts_src = np.array([[float(-70),float(99)], [float(521),float(17)], [float(792),float(103)],[float(68),float(321)]])
 
 
    # Read destination image.
    #im_dst = cv2.imread('book1.jpg')
    # Four corners of the book in destination image.
    pts_dst = np.array([[float(0),float(0)],[float(0),float(600)],[float(300),float(600)],[float(300),float(0)]])
    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
     
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (320,600))
     
    # Display images
    #cv2.imshow("Source Image", im_src)
    #cv2.imshow("Destination Image", im_out)
    

    rows = im_out.shape[0]
    cols = im_out.shape[1]

    #rotation
    M = cv2.getRotationMatrix2D((rows/2,rows/2),-90,1)
    im_out = cv2.warpAffine(im_out,M,(600,320))

    # M = np.float32([[1,0,-cols/2],[0,1,-cols/2]])
    # im_out = cv2.warpAffine(im_out,M,(rows,cols))

    
    im_out = im_out[:,::-1]
    #cv2.imshow("Destination Image", im_out)

    #cv2.imshow("Warped Source Image", im_out)
    cv2.imwrite("2014CarolinaKostnerFS3rect/frame%d.jpg" % i, im_out)
    #cv2.waitKey(0)

if __name__ == '__main__' :
	for i in range(405):
		print i
		run(i)
	#run(3)
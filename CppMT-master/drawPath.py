import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy.misc
from PIL import Image


width = 480
height = 360
channels = 3

img = np.zeros((height, width, channels), dtype=np.uint8)

xpos = []
ypos = []
with open('file.csv', 'r') as inputfile:
	reader = csv.reader(inputfile, delimiter = ',')
	print reader.next()
	for row in reader:
		x = float(row[5])
		y = float(row[6])
		w = float(row[7])
		h = float(row[8])
		#xpos.append(float(row[2]))
		#ypos.append(float(row[3]))
		xpos.append(int(x))
		ypos.append(int(y+h/2))

img = Image.new( 'RGB', (480,360), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(len(xpos)):
	x = xpos[i]
	y = ypos[i]
	print x,y
	if i<50:
		pixels[x,y] = (255,0,0)
	else:
	 	pixels[x,y] = (0,0,0)


#img.show()
img.save('image.png')

im_src = cv2.imread('image.png' )
im_src = np.asarray(im_src)
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
im_out = cv2.warpPerspective(im_src, h, (320,600),flags = cv2.INTER_LINEAR, borderMode = cv2.BORDER_CONSTANT, borderValue = (255,255,255))
 
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
cv2.imwrite("finalpath.jpg" , im_out)




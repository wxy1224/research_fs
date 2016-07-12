import cv2
import numpy as np

count = 0
success = True
while success:

	img=cv2.imread("2014CarolinaKostnerFS3/frame%d.jpg" % count)
	(m,n,c) = img.shape
	print m,n,c


	crop = img[0:m,0:n]
	#(cm,cn,cc) = crop.shape
	for i in range(m):
		for j in range(n):
			if (i<-float(7/20)*j+95) or (i > -float(1/10)*j+200):
				crop[i,j,0] = 0
				crop[i,j,1] = 0
				crop[i,j,2] = 0

	maxi = 0
	maxj = 0
	mini = m
	minj = n
	for i in range(m):
		for j in range(n):
			if img[i,j,0]>100:
				if (i>maxi):
					maxi = i
				if (i<mini):
					mini = i
				if (j>maxj):
					maxj  = j
				if (j<minj):
					minj = j
	print maxi,mini, maxj,minj
	crop = img[mini:maxi,minj:maxj]
	# cv2.imshow('image',crop)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	cv2.imwrite("2014CarolinaKostnerFS3-crop/frame%d.jpg" % count, crop)
	count +=1
	print count
	if count>405:
		break

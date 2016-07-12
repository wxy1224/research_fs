import numpy as np
import cv2
     
cap = cv2.VideoCapture('fancam/2014CarolinaKostnerFS3cut.mp4')
   
fgbg = cv2.BackgroundSubtractorMOG()
   
count = 0
success = True
while(success):
  success, frame = cap.read()
  
  fgmask = fgbg.apply(frame)

  # cv2.imwrite("2014CarolinaKostnerFS3/frame%d.jpg" % count, fgmask)
  # count = count+1
  # print count
  
  cv2.imshow('frame',fgmask)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
      break
  
cap.release()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# #cap = cv2.VideoCapture("fancam/2014CarolinaKostnerFS.mp4")
# cap = cv2.VideoCapture("fancam/20140219YunaKimSP.mp4")   
# ret, frame1 = cap.read()
# prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
# hsv = np.zeros_like(frame1)
# hsv[...,1] = 255
   
# while(1):
  
#   ret, frame2 = cap.read()
#   print frame2.shape
#   cv2.imshow('frame',frame2)
#   if frame2 is not None:
#     break

#   next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
#   flow = cv2.calcOpticalFlowFarneback(prvs,next, 0.5,1,3,15,3,5,1)

#   mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
#   hsv[...,0] = ang*180/np.pi/2
#   hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
#   bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

#   cv2.imshow('frame2',bgr)
#   k = cv2.waitKey(30) & 0xff
#   if k == 27:
#     break
#   elif k == ord('s'):
#     cv2.imwrite('opticalfb.png',frame2)
#     cv2.imwrite('opticalhsv.png',bgr)
#   prvs = next

#   cap.release()
#   cv2.destroyAllWindows()
import cv2

vidcap = cv2.VideoCapture('fancam/2014CarolinaKostnerFS3cut.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print 'Read a new frame: %d' % count
  cv2.imwrite("2014CarolinaKostnerFS3cut/frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
  
import cv2
vidcap = cv2.VideoCapture('datasets/videos/video_2.mp4')
success,image = vidcap.read()
count = 475
while success:
  cv2.imwrite("datasets/images/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
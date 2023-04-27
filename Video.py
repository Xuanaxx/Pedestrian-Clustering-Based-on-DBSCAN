import cv2

fps = 5
size = (640, 480)
frames = 541
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter('video_update_5fps.mp4', fourcc, fps, size)
for filename in ['img_update/{0}.png'.format(i) for i in range(frames)]:
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    video.write(img)
video.release()

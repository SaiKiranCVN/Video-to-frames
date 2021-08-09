#https://stackoverflow.com/questions/18954889/how-to-process-images-of-a-video-frame-by-frame-in-video-streaming-using-openc
import cv2
import os
import shutil

cap = cv2.VideoCapture("./wtc.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("./wtc.mp4")
    cv2.waitKey(1000)
    print("Wait for the header")

pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) # Stating with zero frame
print('Frame Rate = ',cap.get(cv2.CAP_PROP_FPS))
path = 'output_frames' # To save images
if not os.path.exists(path):
    os.makedirs(path)
else:
    shutil.rmtree(path)           # Removes all the subdirectories!
    os.makedirs(path)
os.chdir('./output_frames')
#print(os.getcwd())


while True:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        #cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        # print(str(pos_frame)+" frames")
        cv2.imwrite(str(pos_frame)+'.jpg',frame)
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        #print("frame is not ready")
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break
cap.release()
cv2.destroyAllWindows()




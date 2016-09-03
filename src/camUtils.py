import cv2
import vidUtils
import dirUtils
import filterUtils
import time
import datetime as dt

def startCamera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    while(1):
        cv2.imshow('frame',frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

def startRecording(add_timer = False):
    cap = cv2.VideoCapture(0)
    out1 = vidUtils.configureVideos("processed")
    out2 = vidUtils.configureVideos("original")

    current_time = time.time()

    while(1):

        # Take each frame
        ret, frame = cap.read()

        processed = filterUtils.clearImage(frame)
        date = str(dt.datetime.now())

        if add_timer:
            vidUtils.addTextOnVideo(frame, "Original: " + date, 15, 30)
            vidUtils.addTextOnVideo(processed, "Processed: " + date, 15, 30)

        out2[1].write(frame)
        out1[1].write(processed)

        cv2.imshow('frame',frame)
        cv2.imshow('processed',processed)

        # if time.time() - current_time > 10:
        #     break
        if dirUtils.checkFileSize(out1[0], 3.2):
            print("video size exceeded")


        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    stopAndReleaseRestartRecording(cap, out1, out2)

def stopAndReleaseRestartRecording(cap, out1, out2, start = False):
    cap.release()
    out1[1].release()
    out2[1].release()
    cv2.destroyAllWindows()

    dirUtils.moveVideoToItsDirectory(out1[0] + ".avi", True)
    dirUtils.moveVideoToItsDirectory(out2[0] + ".avi")

    if start:
        startRecording()

def stopRecording():
    cv2.destroyAllWindows()
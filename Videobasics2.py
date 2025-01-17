# For saving the Video

import cv2
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('myvideo.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 20, (width, height))

while True:
    ret, frame = cap.read()
    
    #Operations (Drawing)
    writer.write(frame)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
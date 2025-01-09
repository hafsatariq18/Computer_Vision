import cv2
import numpy as np

# Function to draw circles on mouse events
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)  
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)  

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)


# Create a named window
cv2.namedWindow('my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)


while True:
    cv2.imshow('my_drawing', img) 
    if cv2.waitKey(20) & 0xFF == 27: 
        break

cv2.destroyAllWindows() 

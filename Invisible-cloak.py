import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

# Store a single frame as background 
_, background = cap.read()
time.sleep(2)
_, background = cap.read()

#define all the kernels size  
open_kernel = np.ones((5,5),np.uint8)
close_kernel = np.ones((7,7),np.uint8)
dilation_kernel = np.ones((10, 10), np.uint8)

# Function for remove noise from mask 
def filter_mask(mask):

    close_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernel)
    open_mask = cv2.morphologyEx(close_mask, cv2.MORPH_OPEN, open_kernel)
    dilation = cv2.dilate(open_mask, dilation_kernel, iterations= 1)
    return dilation

while cap.isOpened():
    ret, frame = cap.read()  # Capture every frame
    # convert to hsv colorspace 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # for blue color
    lower_bound = np.array([105, 120, 100])     
    upper_bound = np.array([135, 255, 255])
  
    # for yellow color
    # lower_bound = np.array([25, 120, 100])     
    # upper_bound = np.array([33, 255, 255])

    # for Green color 
    # lower_bound = np.array([45, 120, 100])     
    # upper_bound = np.array([75, 255, 255])

    # for cyan color
    # lower_bound = np.array([87, 120, 100])     
    # upper_bound = np.array([93, 255, 255])

    # for red color
    # lower_bound = np.array([160, 120, 100])     
    # upper_bound = np.array([179, 255, 255])

    # for magneta color
    # lower_bound = np.array([147, 120, 100])     
    # upper_bound = np.array([153, 255, 255])

    # for white color
    # lower_bound = np.array([0, 0, 150]) 
    # upper_bound = np.array([180, 30, 255])

    # for black color
    # lower_bound = np.array([0, 0, 0])     
    # upper_bound = np.array([180, 50, 50])

    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Filter mask
    mask = filter_mask(mask)

    # Apply the mask to take only those region from the saved background 
    # where our cloak is present in the current frame
    cloak = cv2.bitwise_and(background, background, mask=mask)

    # create inverse mask 
    inverse_mask = cv2.bitwise_not(mask)  

    # Apply the inverse mask to take those region of the current frame where cloak is not present 
    current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    # Combine cloak region and current_background region to get final frame 
    combined = cv2.add(cloak, current_background)

    cv2.imshow("Invisible cloak", combined)


    if cv2.waitKey(1) == ord('q'): #for exiting the window
        break
    
cap.release()
cv2.destroyAllWindows()
# Original webcam image capture code from https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
#
# Modifications: Sharon Harrison February 2024
#
# This program enables capture of snapshots for training data purposes
#
# When <space> is pressed, a snapshot is taken and saved sequentially, using img_counter,
# in png format in /homw/vex/FF_Vex/src/training                                                                                                                                         folder
# <ESC> to exit program
#
# Traverse list of images and reduce size of each to reduce processing demands

#vex:disable=repl

import cv2
import os


directory = r'/home/vex/Documents/vex-vscode-projects/nanoSensorsMotors/src/training'
os.chdir(directory)

camera = cv2.VideoCapture(0)
cv2.namedWindow("snapshots")

img_counter = 0
get_more_images = True

while get_more_images == True:
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("webcam", frame)

    k = cv2.waitKey(1)
    if k%256==27:
        #ESC pressed
        print("Closing program")
        get_more_images = False
    elif k%256 == 32:
        # SPACE pressed
        img_name = "image_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} saved".format(img_name))
        img_counter += 1
camera.release()
cv2.destroyAllWindows()

# Images are saved 1280 x 960 which we want to make smaller to reduce training demands on processor
# Let's make them 10% of the original size

for i in range(0, img_counter -1):
    image = cv2.imread("image_{}.png".format(i))
    half_size = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
    new_image = "image_50_{}.png".format(i)
    cv2.imwrite(new_image, half_size) 
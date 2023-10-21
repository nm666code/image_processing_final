# import the necessary packages
from imutils import paths
import argparse
import dlib
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--detector", required=True, help="Path to trained object detector")
ap.add_argument("-d2", "--detector2", required=True, help="Path to trained object detector2")
ap.add_argument("-t", "--testing", required=True, help="Path to directory of testing images")
args = vars(ap.parse_args())
# load the detector
detector = dlib.simple_object_detector(args["detector"])
detector2 = dlib.simple_object_detector(args["detector2"])
# loop over the testing images
for testingPath in paths.list_images(args["testing"]):
    # load the image and make predictions
    image = cv2.imread(testingPath)
    boxes = detector(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    boxes2 = detector2(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # loop over the bounding boxes and draw them
    for b in boxes:
        (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
        cv2.putText(image,'chihuahua', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2,2)
    for b2 in boxes2:
        (x, y, w, h) = (b2.left(), b2.top(), b2.right(), b2.bottom())
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
        cv2.putText(image,'muffin', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2,2)
    # show the image
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
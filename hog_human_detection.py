import cv2
import imutils

# Initialize HOG descriptor
hog = cv2.HOGDescriptor()

# Use pre-trained SVM for people detection
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Load image (change path if needed)
image = cv2.imread("input.jpg")

# Resize image for faster processing
image = imutils.resize(image, width=min(800, image.shape[1]))

# Detect people in image
(rects, weights) = hog.detectMultiScale(
    image,
    winStride=(4, 4),
    padding=(8, 8),
    scale=1.05
)

# Draw bounding boxes
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show output
cv2.imshow("Human Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# HOG Human Detection

This project demonstrates human detection in images using the Histogram of Oriented Gradients (HOG) descriptor and a pre-trained Support Vector Machine (SVM) provided by OpenCV.

## Features
- Detects people in static images
- Draws bounding boxes around detected humans
- Uses OpenCV's built-in HOG + SVM detector

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- imutils

## Installation
Install the required packages using pip:

```
pip install opencv-python imutils
```

## Usage
1. Place your input image in the project directory and rename it to `input.jpg` (or change the filename in the script).
2. Run the script:

```
python hog_human_detection.py
```

3. The script will display the image with detected humans highlighted by green bounding boxes.

## Customization
- To use a different image, change the filename in the script (`cv2.imread("input.jpg")`).
- Adjust detection parameters (e.g., `winStride`, `padding`, `scale`) for different results.

## References
- [OpenCV HOG Descriptor Documentation](https://docs.opencv.org/4.x/d5/d33/structcv_1_1HOGDescriptor.html)
- [imutils Documentation](https://pypi.org/project/imutils/)

---

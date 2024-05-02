import cv2
import numpy as np

def count_circles(image):
  # Convert the image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply Gaussian blur to reduce noise
  blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

  # Detect circles using Hough Circle Transform
  circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20)

  # Count the number of circles
  num_circles = 0
  if circles is not None:
    for circle in circles[0]:
      num_circles += 1

  return num_circles

# Read the image
image = cv2.imread('circle.png')

# Count the number of circles
num_circles = count_circles(image)

# Print the number of circles
print(f"Number of circles: {num_circles}")

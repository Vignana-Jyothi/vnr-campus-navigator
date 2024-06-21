import cv2
import numpy as np
import random

# Function to generate a random color
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Load the image
image_path = 'output-1.png'  
img = cv2.imread(image_path)

# Check if image is loaded successfully
if img is None:
    print(f"Error: Unable to load image at {image_path}")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter and draw bounding boxes around detected rooms
room_boxes = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if 1000 < w*h < 500000:  # Adjust size filter based on room sizes in the image
        room_boxes.append((x, y, x+w, y+h))
        color = get_random_color()
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

# Save the annotated image
output_image_path = 'annotated_image2.png'  # Update this path
cv2.imwrite(output_image_path, img)

# Display the annotated image (optional)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the room coordinates
for i, (x1, y1, x2, y2) in enumerate(room_boxes):
    print(f"Room {i+1}: ({x1}, {y1}, {x2}, {y2})")

print(f"Annotated image saved to {output_image_path}")

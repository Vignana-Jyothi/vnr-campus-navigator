import cv2
import numpy as np
import random
import pyperclip

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

# Draw the initial bounding boxes
annotated_img = img.copy()
for (x1, y1, x2, y2) in room_boxes:
    color = get_random_color()
    cv2.rectangle(annotated_img, (x1, y1), (x2, y2), color, 2)

# Mouse callback function to handle clicks
def select_room(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_rooms = [box for box in room_boxes if box[0] <= x <= box[2] and box[1] <= y <= box[3]]
        if selected_rooms:
            selected_img = img.copy()
            for box in selected_rooms:
                cv2.rectangle(selected_img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.imshow('Select Room', selected_img)
            
            # Wait for the user to select a room
            room_idx = int(input(f"Select a room by entering the index (0 to {len(selected_rooms) - 1}): "))
            if 0 <= room_idx < len(selected_rooms):
                selected_box = selected_rooms[room_idx]
                coordinates_str = f"{selected_box[0]},{selected_box[1]},{selected_box[2]},{selected_box[3]}"
                pyperclip.copy(coordinates_str)
                print(f"Coordinates {coordinates_str} copied to clipboard.")

# Display the image and set mouse callback
cv2.imshow('Annotated Image', annotated_img)
cv2.setMouseCallback('Annotated Image', select_room)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the annotated image
output_image_path = 'annotated_image2.png'
cv2.imwrite(output_image_path, annotated_img)
print(f"Annotated image saved to {output_image_path}")

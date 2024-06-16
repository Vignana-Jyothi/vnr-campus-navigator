import cv2
from PIL import Image
import random

# Load the image
image_path = 'example_floor_map.jpg'
image = cv2.imread(image_path)

# Coordinates of the rooms to highlight (example: room 202)
# These coordinates need to be determined manually or through some form of automation
room_coordinates = {
    '202': (10, 50, 90, 60),  # (x1, y1, w, h)
    '204': (10, 110, 90, 60),  # (x1, y1, w, h)
    '206': (10, 170, 90, 60),  # (x1, y1, w, h)
    '208': (15, 230, 85, 60),  # (x1, y1, w, h)
    '210': (15, 290, 85, 55),  # (x1, y1, w, h) fixed
    '212': (15, 345, 85, 85),  # (x1, y1, w, h)  
    '214': (15, 430, 85, 85),  # (x1, y1, w, h)  
    '216': (15, 515, 85, 85),  # (x1, y1, w, h)  
    '218': (10, 600, 55, 110),  # (x1, y1, w, h)      
    '203': (120, 50, 90, 60),  # (x1, y1, w, h)
    '205': (120, 110, 90, 60),  # (x1, y1, w, h)
    '207': (120, 170, 90, 60),  # (x1, y1, w, h)
    '209': (120, 230, 90, 70),  # (x1, y1, w, h)
    
    # Add coordinates for other rooms as needed
}

def color_room(room_to_highlight, r, g, b):
    # Highlight the room by drawing a rectangle
    if room_to_highlight in room_coordinates:
        (x1, y1, w, h) = room_coordinates[room_to_highlight]
        cv2.rectangle(image, (x1, y1), (x1 + w, y1 + h), (r, g, b), 2)  # Rectangle with specified color and thickness

# Iterate through all rooms and highlight them with random colors
for room in room_coordinates.keys():
    # Generate random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_room(room, r, g, b)

# Save the highlighted image
highlighted_image_path = '/tmp/example_floor_map.jpg'
cv2.imwrite(highlighted_image_path, image)

# Display the image (optional)
highlighted_image = Image.open(highlighted_image_path)
highlighted_image.show()


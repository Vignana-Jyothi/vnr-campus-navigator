import cv2
import random

# Load the image
image_path = '/home/kp/Downloads/Example_FloorMap.jpeg'
image = cv2.imread(image_path)

# Coordinates of the rooms to highlight (example: room 202)
room_coordinates = {
    '202': (10, 50, 90, 60),  # (x1, y1, w, h)
    '204': (10, 110, 90, 60),  # (x1, y1, w, h)
    '206': (10, 170, 90, 60),  # (x1, y1, w, h)
    '208': (15, 230, 85, 60),  # (x1, y1, w, h)
    '210': (15, 290, 85, 55),  # (x1, y1, w, h)
    '212': (15, 345, 85, 85),  # (x1, y1, w, h)
    '214': (15, 430, 85, 85),  # (x1, y1, w, h)
    '216': (15, 515, 85, 85),  # (x1, y1, w, h)
    '218': (10, 600, 55, 105),  # (x1, y1, w, h)
    '203': (120, 50, 90, 60),  # (x1, y1, w, h)
    '205': (120, 110, 90, 60),  # (x1, y1, w, h)
    '207': (120, 170, 90, 60),  # (x1, y1, w, h)
    '209': (120, 230, 90, 60),  # (x1, y1, w, h)
    # Add coordinates for other rooms as needed
}

# Dictionary to store room colors
room_colors = {room: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for room in room_coordinates}

def draw_highlighted_image(mouse_x, mouse_y):
    highlighted_image = image.copy()
    for room, (x1, y1, w, h) in room_coordinates.items():
        if x1 <= mouse_x <= x1 + w and y1 <= mouse_y <= y1 + h:
            cv2.rectangle(highlighted_image, (x1, y1), (x1 + w, y1 + h), (0, 255, 255), 3)  # Highlight with a specific color
        else:
            cv2.rectangle(highlighted_image, (x1, y1), (x1 + w, y1 + h), room_colors[room], 2)  # Default color
    return highlighted_image

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        highlighted_image = draw_highlighted_image(x, y)
        cv2.imshow("Floor Map", highlighted_image)

# Create a window and set the mouse callback
cv2.namedWindow("Floor Map")
cv2.setMouseCallback("Floor Map", mouse_callback)

# Initial display
cv2.imshow("Floor Map", image)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import json
import numpy as np

# Load JSON data
json_path = 'ABC_floor1.json'  
with open(json_path, 'r') as f:
    rooms_data = json.load(f)

# Initialize global variables
drawing = False
ix, iy = -1, -1
rectangles = [(None, None, None, None)] * len(rooms_data)
current_room_index = 0

# Function to draw rectangle on mouse callback
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, current_room_index, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        rectangles[current_room_index] = (ix, iy, x, y)
        print(f"Coordinates for {rooms_data[current_room_index]['room_number']} saved: {(ix, iy, x, y)}")

# Function to save annotated rectangles to JSON
def save_annotations():
    for i, rect in enumerate(rectangles):
        if rect != (None, None, None, None):
            rooms_data[i]['coordinates'] = rect
    
    with open('annotated_rooms.json', 'w') as f:
        json.dump(rooms_data, f, indent=4)
    print("Annotations saved to annotated_rooms.json")

# Load the image
image_path = 'output-1.png' 
img = cv2.imread(image_path)

# Check if image is loaded successfully
if img is None:
    print(f"Error: Unable to load image at {image_path}")
    exit()

# Function to update the displayed image
def update_display():
    global img, rectangles, current_room_index
    img_copy = img.copy()
    if rectangles[current_room_index] != (None, None, None, None):
        (ix, iy, x, y) = rectangles[current_room_index]
        cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 0, 255), 2)  # Red rectangle for existing
    cv2.imshow('image', img_copy)

# Create a window and set mouse callback for drawing rectangles
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

print(f"Annotating room: {rooms_data[current_room_index]['room_number']}")
update_display()

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        save_annotations()
        break
    elif key == ord('n'):
        if current_room_index < len(rooms_data) - 1:
            current_room_index += 1
            print(f"Annotating room: {rooms_data[current_room_index]['room_number']}")
            update_display()
    elif key == ord('p'):
        if current_room_index > 0:
            current_room_index -= 1
            print(f"Annotating room: {rooms_data[current_room_index]['room_number']}")
            update_display()

cv2.destroyAllWindows()

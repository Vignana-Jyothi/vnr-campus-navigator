import cv2
import json
import numpy as np
from pynput import keyboard

# Load JSON data
json_path = 'ABC_floor1.json'  # Update this path if necessary
with open(json_path, 'r') as f:
    rooms_data = json.load(f)

# Initialize global variables
drawing = False
ix, iy = -1, -1

# Extract rectangles directly from rooms_data
rectangles = [tuple(room["coordinates"]) for room in rooms_data]

current_room_index = 0
ctrl_pressed = False

# Function to draw rectangle on mouse callback
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, current_room_index, img, rectangles, ctrl_pressed
    
    if ctrl_pressed:
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
    
    with open('ABC_floor1.json', 'w') as f:
        json.dump(rooms_data, f, indent=4)
    print("Annotations saved to ABC_floor1.json")

# Load the image
image_path = 'output-1.png'  # Update this path if necessary
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
    # Display current room number
    room_number_text = rooms_data[current_room_index]['room_number']
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = 2
    text_thickness = 3
    text_color = (255, 0, 0)  # Blue color in BGR
    text_position = (img.shape[1] // 2 - 100, 50)  # Adjust position as needed
    cv2.putText(img_copy, room_number_text, text_position, font, text_size, text_color, text_thickness, cv2.LINE_AA)
    cv2.imshow('image', img_copy)

# Function to handle key press events
def on_press(key):
    global ctrl_pressed
    try:
        if key == keyboard.Key.ctrl:
            ctrl_pressed = True
    except AttributeError:
        pass

# Function to handle key release events
def on_release(key):
    global ctrl_pressed
    try:
        if key == keyboard.Key.ctrl:
            ctrl_pressed = False
    except AttributeError:
        pass

# Create a window and set mouse callback for drawing rectangles
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

print(f"Annotating room: {rooms_data[current_room_index]['room_number']}")
update_display()

# Start listening to keyboard events
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

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
    elif key == 2555904:  # Right arrow key
        if current_room_index < len(rooms_data) - 1:
            current_room_index += 1
            print(f"Annotating room: {rooms_data[current_room_index]['room_number']}")
            update_display()
    elif key == 2424832:  # Left arrow key
        if current_room_index > 0:
            current_room_index -= 1
            print(f"Annotating room: {rooms_data[current_room_index]['room_number']}")
            update_display()

cv2.destroyAllWindows()
listener.stop()

import cv2
import json

# Initialize list to store annotations
annotations = []

# Function to draw rectangle and capture metadata
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img

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
        room_number = input("Enter room number: ")
        room_type = input("Enter room type: ")
        floor_number = input("Enter floor number: ")
        annotations.append({
            'coordinates': (ix, iy, x, y),
            'room_number': room_number,
            'room_type': room_type,
            'floor_number': floor_number
        })
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        cv2.imshow('image', img)

# Load image
image_path = 'output-1.png'
img = cv2.imread(image_path)

# Initialize global variables
ix, iy = -1, -1
drawing = False

# Set up the window and the mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# Display the image and wait for user input
while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Save annotations to a JSON file
with open('annotations.json', 'w') as f:
    json.dump(annotations, f, indent=4)

print("Annotations saved to annotations.json")

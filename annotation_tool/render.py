import cv2
import json
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

# Load room data from JSON file
json_path = 'ABC_floor1.json'  # Update this path
with open(json_path, 'r') as f:
    rooms_metadata = json.load(f)

# Define colors for each room type
room_colors = {
    "Classroom": get_random_color(),
    "Lab": get_random_color(),
    "Toilet": get_random_color(),
    "Staff Room": get_random_color(),
    "Faculty Room": get_random_color(),
    "HOD Room": get_random_color(),
    "Library": get_random_color(),
    "Office": get_random_color()
}

# Annotate each room on the image
for room in rooms_metadata:
    room_type = room["type"]
    coordinates = room["coordinates"]
    color = room_colors.get(room_type, (255, 255, 255))  # Default to white if type not found
    cv2.rectangle(img, (coordinates[0], coordinates[1]), (coordinates[2], coordinates[3]), color, 2)
    cv2.putText(img, room["room_number"], (coordinates[0], coordinates[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Save the annotated image
output_image_path = 'annotated_image.png'  # Update this path
cv2.imwrite(output_image_path, img)

# Display the annotated image (optional)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Annotated image saved to {output_image_path}")

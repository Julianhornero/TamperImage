from PIL import Image
import numpy as np

# Load image
image_path = 'input_image.jpg'
image = Image.open(image_path)

# Convert to NumPy array
image_np = np.array(image)

# Example tampering: Change a rectangular region to white
# Define the region coordinates (top-left and bottom-right)
x_start, y_start = 50, 50
x_end, y_end = 150, 150

# Modify pixels in the region to white (255, 255, 255)
image_np[y_start:y_end, x_start:x_end] = [255, 255, 255]

# Convert back to image
tampered_image = Image.fromarray(image_np)

# Save tampered image
tampered_image.save('tampered_image.jpg')


# TamperImage

**TamperImage** is a simple Python tool to manipulate the pixel data of an image to simulate tampering. This can be useful for testing image forensics, tamper detection algorithms, or just for educational purposes.

## Features

- Load an image and manipulate specific pixel regions
- Simulate tampering by modifying colors or regions in the image
- Save the tampered image for further use or analysis
- Lightweight and easy to use with minimal dependencies

## Installation

Make sure you have Python 3.x installed. Then, install the required dependencies:

```
pip install pillow numpy
```

## Usage

1. Clone the repository or download the script:

```
git clone https://github.com/Julianhornero/TamperImage.git
cd TamperImage
```

2. Use the provided script or your own Python code to tamper with images. Here is a simple example:

```
from PIL import Image
import numpy as np

# Load image
image = Image.open('input_image.jpg')
image_np = np.array(image)

# Define tampering region (x_start, y_start, x_end, y_end)
x_start, y_start = 50, 50
x_end, y_end = 150, 150

# Tamper region by setting pixels to white
image_np[y_start:y_end, x_start:x_end] = 

# Save tampered image
tampered_image = Image.fromarray(image_np)
tampered_image.save('tampered_image.jpg')
```

## Example

Original image | Tampered image  
:-------------------------:|:-------------------------:  
![original](examples/original.jpg) | ![tampered](examples/tampered.jpg)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


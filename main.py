from rembg import remove
from PIL import Image

input_path = 'rita.jpg'
output_path = 'rita_newres.png'

# Open the image
image = Image.open(input_path)

# Remove the image background using rembg library
processed_image = remove(image)

# Save the processed image as PNG
processed_image.save(output_path, 'PNG')

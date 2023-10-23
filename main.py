from rembg import remove
from PIL import Image

input_path = 'rita.jpg'
output_path = 'rita_newres.png'


image = Image.open(input_path)


processed_image = remove(image)


processed_image.save(output_path, 'PNG')

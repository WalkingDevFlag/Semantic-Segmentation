import os
from PIL import Image
import math

def patch_images(input_dir):
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg') or f.endswith('.png')]
    
    # Calculate the number of rows and columns needed for the square image
    num_images = len(image_files)
    num_rows = int(math.sqrt(num_images))
    num_cols = num_rows
    
    # Get the size of the first image
    first_image = Image.open(os.path.join(input_dir, image_files[0]))
    image_width, image_height = first_image.size
    
    # Create a new image to hold the patched-up image
    patch_width = num_cols * image_width
    patch_height = num_rows * image_height
    patched_image = Image.new('RGB', (patch_width, patch_height))
    
    # Paste the segmented images into the patched image
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path)
        row = i // num_cols
        col = i % num_cols
        x = col * image_width
        y = row * image_height
        patched_image.paste(image, (x, y))
    
    return patched_image

# Example usage
input_dir = 'E:\Random Python Scripts\FarmLand-Segmentation-main\Semantic Segmentation Dataset\Tile 8\masks'
patched_image = patch_images(input_dir)
patched_image.save('patched_mask_8.jpg')

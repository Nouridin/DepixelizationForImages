from PIL import Image

def enhance_image(image_path):
    with Image.open(image_path) as img:

    enhanced_img = img.convert("L")
    return enhanced_img
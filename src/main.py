from PIL import Image
import sys
import os
from imgProcessor import enhance_image

def main(image_path):
    if not os.path.isfile(image_path):
        print("Error: File does not exist.")
        return

    enhanced_image = enhanced_image(image_path)

    output_path = f"enhanced_{os.path.basename(image_path)}" 
    enhanced_image.save(output_path)

    print(f"Enhanced image saved as {outpath_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)
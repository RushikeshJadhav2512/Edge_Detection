import cv2
from PIL import Image
import numpy as np
import os
import sys

def main():
    input_path = 'istockphoto-1420676204-1024x1024.jpg'
    output_dir = 'output'
    output_path = os.path.join(output_dir, 'Edge_Sample_Canny.png')

    if not os.path.exists(input_path):
        print(f"Error: Input image not found at {input_path}")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = cv2.imread(input_path, flags=0)
    img_u8 = img.astype(np.uint8)

    img_blur = cv2.GaussianBlur(img_u8, (3, 3), 0, 0)
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

    # edges is a single channel image, no need to convert color
    pil_image = Image.fromarray(edges)
    pil_image.save(output_path)
    print(f"Canny edge detection image saved to {output_path}")

if __name__ == "__main__":
    main()

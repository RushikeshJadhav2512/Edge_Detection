import cv2
import numpy as np
from PIL import Image
import os
import sys

def main():
    input_path = 'istockphoto-1420676204-1024x1024.jpg'
    print(f"Reading image from: {input_path}")
    output_dir = 'output'
    output_pathX = os.path.join(output_dir, 'Edge_Sample_SobelX.png')
    output_pathY = os.path.join(output_dir, 'Edge_Sample_SobelY.png')
    output_pathXY = os.path.join(output_dir, 'Edge_Sample_SobelXY.png')

    if not os.path.isfile(input_path):
        print(f"Error: Input image not found at {input_path}")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = cv2.imread(input_path, flags=0)
    if img is None:
        print(f"Error: Failed to load image at {input_path}")
        sys.exit(1)

    img_u8 = img.astype(np.uint8)

    img_blur = cv2.GaussianBlur(img_u8, (3, 3), 0, 0)

    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    abs_sobelx = np.absolute(sobelx)
    abs_sobely = np.absolute(sobely)
    abs_sobelxy = np.absolute(sobelxy)

    sobelx_8u = np.uint8(abs_sobelx)
    sobely_8u = np.uint8(abs_sobely)
    sobelxy_8u = np.uint8(abs_sobelxy)

    pil_imageX = Image.fromarray(sobelx_8u)
    pil_imageX.save(output_pathX)

    pil_imageY = Image.fromarray(sobely_8u)
    pil_imageY.save(output_pathY)

    pil_imageXY = Image.fromarray(sobelxy_8u)
    pil_imageXY.save(output_pathXY)

    print(f"Sobel edge detection images saved to {output_dir}")

if __name__ == "__main__":
    main()

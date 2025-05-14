from PIL import Image, ImageFilter
import os
import sys

def main():
    input_path = '_.jpeg'
    output_dir = 'output'
    output_path = os.path.join(output_dir, 'EDGE_sample1.png')

    if not os.path.exists(input_path):
        print(f"Error: Input image not found at {input_path}")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(input_path)

    # Converting the image to grayscale, as Sobel Operator requires
    # input image to be of mode Grayscale (L)
    img = img.convert("L")

    # Calculating Edges using the passed laplacian Kernel
    final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
                                                -1, -1, -1, -1), 1, 0))

    final.save(output_path)
    print(f"Laplacian edge detection image saved to {output_path}")

if __name__ == "__main__":
    main()

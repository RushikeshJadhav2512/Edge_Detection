from PIL import Image, ImageFilter
import os
import sys

def main(): 
    input_path = '_.jpeg'
    output_dir = 'output'
    output_path = os.path.join(output_dir, 'Edge_Sample.png')

    if not os.path.exists(input_path):
        print(f"Error: Input image not found at {input_path}")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = Image.open(input_path)

    # Converting the image to grayscale, as edge detection requires input image to be of mode = Grayscale (L)
    image = image.convert("L")

    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    image = image.filter(ImageFilter.FIND_EDGES)

    # Saving the Image Under the name Edge_Sample.png
    image.save(output_path)
    print(f"Edge detection image saved to {output_path}")

if __name__ == "__main__":
    main()

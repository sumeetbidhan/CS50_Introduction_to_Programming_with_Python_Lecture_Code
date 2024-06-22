import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) !=3:
        print("Usage: python shirt.py <input_image> <output_image>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    valid_extensions = ['.jpg','.jpeg','.png']
    input_ext = os.path.splittext(input_filename)[1].lower()
    output_ext = os.path.splittext(output_filename)[1].lower()

    if input_ext not in valid_extensions:
        print("Invalid input format")
        sys.exit(1)

    if output_ext not in valid_extensions:
        print("Invalid output format")
        sys.exit(1)

    if input_ext != output_ext:
        print("Input and output have different extensions")
        sys.exit(1)

    if not os.path.isfile(input_filename):
        print("Input does not exist")
        sys.exit(1)

    try:
        input_image = Image.open(input_filename)
        shirt = Image.open("shirt.png")

        shirt_size = shirt.size

        input_image = ImageOps.fit(input_image, shirt_size)

        input_image.paste(shirt, shirt)

        input_image.save(output_filename)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    try:
        image = Image.open(arg)
        images.append(image)
    except IOError:
        print(f"Cannot open {arg}")

if len(images) > 1:
    images[0].save(
        "costumes.gif", save_all=True, append_images=images[1:], duration=200, loop=0
    )
    print("GIF created successfully!")
else:
    print("Please provide at least two valid image files to create a GIF.")

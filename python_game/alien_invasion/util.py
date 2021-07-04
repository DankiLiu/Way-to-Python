from PIL import Image


def image_to_bitmap(image):
    """Convert image into bitmap."""
    img = Image.open(image)
    print("image format is ", img.format)

    # Resize image
    img = img.resize((50, 50))

    if img.format != "BMP":
        print("Converting image to BMP format.")
        image = image.split('.')[0] + '.bmp'
        img.save(image)
    return image


def resize_image(image):
    img = Image.open(image)
    # Resize image
    img = img.resize((80, 80))
    img.save(image)


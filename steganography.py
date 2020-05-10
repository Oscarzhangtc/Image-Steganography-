"""A program that encodes and decodes hidden messages in images through LSB steganography
    competed by: Oscar Zhang
"""
from PIL import Image, ImageFont, ImageDraw
import textwrap


def decode_image(file_location="images/encoded_sample.png"):
    """Decodes the hidden message in an image.

    Parameters
    ----------
    file_location: str
        The location of the image file to decode. This defaults to the provided
        encoded image in the images folder.
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]


    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]


    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    for x in range(x_size):
        for y in range(y_size):
            red_pixel = red_channel.getpixel((x,y))
            binary = bin(red_pixel)

            lsb = int(binary[-1])
            if(lsb == 0):
                pixels[x,y] = (0,0,0)
            elif(lsb == 1):
                pixels[x,y] = (255,255,255)

    pass
    decoded_image.save("images/decoded_image.png")


def write_text(text_to_write, image_size):
    """Write text to an RGB image. Automatically line wraps.

    Parameters
    ----------
    text_to_write: str
        The text to write to the image.
    image_size: (int, int)
        The size of the resulting text image.
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    # Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin, offset), line, font=font)
        offset += 10
    return image_text


def encode_image(text_to_encode, template_image="images/template_image.jpg"):
    """Encode a text message into an image.

    Parameters
    ----------
    text_to_encode: str
        The text to encode into the template image.
    template_image: str
        The image to use for encoding. An image is provided by default.
    """
    raw_image = Image.open(template_image)
    hidden_message = write_text(text_to_encode,raw_image.size)

    x_size  = raw_image.size[0]
    y_size  = raw_image.size[1]

    red_channel = raw_image.split()[0]
    green_channel = raw_image.split()[1]
    blue_channel = raw_image.split()[2]
    # get all channels from raw_image
    encoded_image = Image.new("RGB", raw_image.size)

    for x in range(x_size):
        for y in range(y_size):
            hidden_pixel = hidden_message.getpixel((x, y))

            encoded_red_pixel = red_channel.getpixel((x, y))
            if (hidden_pixel == (255, 255, 255)):
                red_channel_pixel = red_channel.getpixel((x, y))
                red_binary = bin(red_channel_pixel)
                red_binary = red_binary[:-1] + "1"
                # change the last binary value
                encoded_red_pixel = int(red_binary,2)
                # covert binary back to int

            else: # if pixel doesnt = white, that means theres no value, set last binary = 0
                red_channel_pixel = red_channel.getpixel((x, y))
                red_binary = bin(red_channel_pixel)
                red_binary = red_binary[:-1] + "0"
                encoded_red_pixel = int(red_binary,2)

            encoded_rgb = (encoded_red_pixel,
                           green_channel.getpixel((x, y)),
                           blue_channel.getpixel((x, y)))

            encoded_image.putpixel((x, y), encoded_rgb)
    encoded_image.save("images/hidden_message_image.png")


if __name__ == '__main__':
    print("Decoding the image...")
    decode_image()

    print("Encoding the image...")
    encode_image()

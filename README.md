
# Image Steganography

This program encodes messages into images and decodes hidden messages from images.

# Guide and Usage

Make sure [python 3](https://www.python.org/downloads/) is installed on your device. 

We will be manipulating and utilizing the Red channel of the RGB colors channels to pass secret messages. 
To begin, a purely black and white image (not grayscale) is an easy thing to conceptualize, where a black pixel has a value of 1 and a white pixel as a value of 0.

Color images have three color channels (RGB), with pixel values of 0-255 for each pixel. So a pixel with the value (255,255,255) would be entirely white while (0,0,0) would be black. The upper range is 255 because it is the largest value that can be represented by an 8 bit binary number such as 0b10001011 or 0b10001011. On the 8 bit binary scale leftmost bit place matters a lot more than rightmost bit because the rightmost bit only modifies the value of the number by 1. 

##### Decode an Image

Provided as an example in the image folder is an image name encoded_sample. It is also the default the argument for decode_image function. The secret image was hidden in the LSB of the pixels in the red channel of the image. That is, the value of the LSB of each red pixel is 1 if the hidden image was 1 at that location, and 0 if the hidden image was also 0. To see the hidden image, simply import the image function from `steganography.py` and run:
```python
`decode_image(file_location="images/encoded_sample.png")`.
```

##### Encode an Image
The `encode_image` function, like its name, encodes an image with your secret message. Hence, requires 2 arguments: a message of your choice, and the image you want to encode the message in. 
It outputs the encoded image named `hidden_message_image.png` to your directory. 
Simply run: 
```python
encode_image(text_to_encode, "images/my_image.jpg")
```
Of course, you will also be able to use the `decode_image()` on your encoded image!






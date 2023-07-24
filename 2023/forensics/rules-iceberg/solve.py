from PIL import Image

def decode_lsb(original_image_path, encoded_image_path):
    # diff the bits of the two images
    original_image = Image.open(original_image_path)
    encoded_image = Image.open(encoded_image_path)
    original_pixels = original_image.load()
    encoded_pixels = encoded_image.load()
    decoded_message = ""
    for y in range(original_image.height):
        if len(decoded_message) > 54 * 8:
            break
        for x in range(original_image.width):
            if len(decoded_message) > 54 * 8:
                break
            r1, g1, b1, a1 = original_pixels[x, y]
            r2, g2, b2, a2 = encoded_pixels[x, y]
            if r1 > g1 and r1 > b1:
                decoded_message += str(format(r2, '08b')[6])
    # convert the binary string to ascii
    return ''.join(chr(int(decoded_message[i:i+8], 2)) for i in range(0, len(decoded_message), 8))

# Decode the hidden message from the image
decoded_message = decode_lsb("rules-iceberg.png","new-rules-iceberg.png")
print("Decoded message:", decoded_message)

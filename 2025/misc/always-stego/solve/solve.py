from PIL import Image

def red_frequencies(img):
    freq = [0]*256
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            freq[r] += 1
    return freq

def main():
    img = Image.open("image.png").convert("RGB")

    print(''.join([chr(i)for i in red_frequencies(img)[::2]]))

if __name__ == "__main__":
    main()

from PIL import Image
import random

def load_text_bytes(path):
    with open(path, "rb") as f:
        data = f.read()
    return list(data)

def red_frequencies(img):
    freq = [0]*256
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            freq[r] += 1
    return freq


def apply_changes(img, text_bytes):
    """
    Modify pixels so that at indices start, start+2, ..., we achieve
    red values equal to ASCII bytes.
    We change as few pixels as possible.
    """
    pixels = img.load()
    w, h = img.size
    freqs = red_frequencies(img)

    # Build mapping from needed red values to their target frequency increases
    need_count = {}
    for i, b in enumerate(text_bytes):
        idx = 50 + 2*i
        need_count[idx] = freqs[idx] - b

    # For each needed red value, modify pixels until freq satisfied
    # We scan pixels randomly to distribute changes.
    coords = [(x, y) for x in range(w) for y in range(h)]
    random.shuffle(coords)

    for target_r, needed_times in need_count.items():
        remaining = needed_times

        for (x, y) in coords:
            if remaining == 0:
                break
            r, g, b = pixels[x, y][:3]
            if r == target_r:
                pixels[x, y] = (r + 1, g, b)
                remaining -= 1

    return img


def main():
    text_bytes = load_text_bytes("flag.txt")
    img = Image.open("image.png").convert("RGB")


    img = apply_changes(img, text_bytes)
    img.save("output.png")
    print("output.png saved.")

if __name__ == "__main__":
    main()

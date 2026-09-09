#!/usr/bin/env python3

import sys
from PIL import Image


def brightness(pixel):
    r, g, b = pixel[:3]
    return r + g + b


def sort_row(row):
    return sorted(row, key=brightness)


def sort_image(image):
    pixels = image.load()

    for y in range(image.height):
        row = [
            pixels[x, y]
            for x in range(image.width)
        ]

        sorted_row = sort_row(row)

        for x, pixel in enumerate(sorted_row):
            pixels[x, y] = pixel

    return image


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 sorter.py input.jpg output.jpg")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    image = Image.open(source).convert("RGB")

    print(f"Processing {source}...")

    result = sort_image(image)
    result.save(destination)

    print(f"Done.")
    print(f"Saved to {destination}")


if __name__ == "__main__":
    main()

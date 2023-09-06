# type: ignore
import os

from PIL import Image


def convert_img(in_ext, out_ext):
    # get list of files from current directory
    files = os.listdir(".")

    # filter list of files by extension, take only needed
    images = [i for i in files if i.endswith(in_ext)]

    # convert each image
    try:
        for image in images:
            img = Image.open(image)
            if img.mode != "RGB":
                img = img.convert("RGB")
            base = os.path.splitext(image)[0]
            img.save(f"{base}{out_ext}")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    convert_img(".png", ".jpg")

# type: ignore
import os

from PIL import Image, ImageDraw, ImageFont


def convert_img_draw(in_ext, out_ext):
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

            # create ImageDraw object
            draw = ImageDraw.Draw(img)

            # define text and font
            text = "Hello,\nWorld!"
            font = ImageFont.truetype("JetBrainsMonoNerdFont-Regular.ttf", 18)

            # calculate width and height of the text
            textwidth = draw.textlength("Hello, world!")
            left, top, right, bottom = draw.multiline_textbbox((0, 0), "Hello,\nworld!")
            textwidth, textheight = right - left, bottom - top

            # calculate width and height of the image
            width, height = img.size

            # ("-10" is a little hack to center the text)
            x = (width - textwidth) / 2
            y = (height - textheight) / 2 - 15

            # draw the text on the image
            draw.multiline_text((x, y), text, font=font, fill="white")
            # path without extension
            base = os.path.splitext(image)[0]
            # save the image
            img.save(f"{base}{out_ext}")
            # del the draw
            del draw

    except Exception as error:
        print(error)


if __name__ == "__main__":
    convert_img_draw(".png", ".jpg")

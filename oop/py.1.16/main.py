# type: ignore
import os
from zipfile import ZipFile


def add_to_zip(zip_name, ext):
    if not zip_name.endswith(".zip"):
        zip_name += ".zip"
    if not ext.startswith("."):
        ext = "." + ext
    with ZipFile(zip_name, "w") as zip_file:
        for root, dirs, files in os.walk("."):
            # only for current directory
            if root == ".":
                for file in files:
                    if file.endswith(ext):
                        zip_file.write(os.path.join(root, file))


zip_name = input("Enter the name of the zip file: ")
ext = input("Enter the extension: ")

if __name__ == "__main__":
    add_to_zip(zip_name, ext)

# type: ignore
import os


def delete_directory(dir_path: str) -> bool:
    # check if path exists
    if not os.path.exists(dir_path):
        print(f"Directory {dir_path} does not exist")
        return False

    # check if path is a directory
    if not os.path.isdir(dir_path):
        print(f"Path {dir_path} is not a directory")
        return False

    # getting list of files and subdirectories
    items = os.listdir(dir_path)

    # check if directory has subdirectories
    for item in items:
        if os.path.isdir(os.path.join(dir_path, item)):
            print(f"Directory {dir_path} has subdirectories")
            return False

    # del all files in directory
    for item in items:
        os.remove(os.path.join(dir_path, item))

    # del dir
    os.rmdir(dir_path)
    print(f"Directory {dir_path} has been deleted")
    return True


print(delete_directory("del/del2/del2.md"))

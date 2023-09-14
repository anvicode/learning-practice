# type: ignore
import os

from ls import get_files_subdirs_list


def delete_directory(dir_path: str) -> bool:
    scan = get_files_subdirs_list(dir_path, "md", False)

    # if it has subdirectories
    if len(scan[1]) > 0:
        return Exception("Error: Directory has subdirectories")

    # del all files in directory
    try:
        for item in scan[0]:
            os.remove(item)
    except Exception as err:
        return err

    # del dir
    try:
        os.rmdir(dir_path)
    except Exception as err:
        return err
    return True


# print(delete_directory("del/del2"))
print(delete_directory("del/del2/del2.md"))

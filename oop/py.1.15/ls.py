# type: ignore
import os


def get_files_subdirs_list(path: str, ext: str, flag: bool) -> list[list[str]]:
    files_list = []
    dirs_list = []

    for root, dirs, files in os.walk(path):
        # if root == path or (flag and separator in path <= 1):
        # it is the limit the depth of the search
        if root == path or (flag and root.count(os.sep) <= path.count(os.sep) + 1):
            for file in files:
                if file.endswith("." + ext):
                    files_list.append(os.path.join(root, file))
            for dir in dirs:
                dirs_list.append(os.path.join(root, dir))
        else:
            break

    return [files_list, dirs_list]


print(get_files_subdirs_list(".", "md", True))
print(get_files_subdirs_list("ls", "md", True))
print(get_files_subdirs_list("ls/sub_ls", "md", True))
print(get_files_subdirs_list("ls/sub_ls/ss_ls", "md", True))

print(get_files_subdirs_list(".", "md", False))
print(get_files_subdirs_list("ls", "md", False))
print(get_files_subdirs_list("ls/sub_ls", "md", False))
print(get_files_subdirs_list("ls/sub_ls/ss_ls", "md", False))

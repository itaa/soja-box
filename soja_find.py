import fnmatch
import os


def find_files(path, types):
    """
    Find files from path with types
    :param path: Where you will find.
    :param types: Which types you will find.
    :return: files
    """
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for extensions in types:
            for filename in fnmatch.filter(filenames, extensions):
                matches.append(os.path.join(root, filename))
    return matches

if __name__ == '__main__':
    my_python_files = find_files('./', ['*.py'])
    print(my_python_files)

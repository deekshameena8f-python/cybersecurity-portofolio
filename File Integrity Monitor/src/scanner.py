import os


def get_files(directory):
    files = []

    for root, dirs, filenames in os.walk(directory):
        for file in filenames:
            files.append(
                os.path.join(root, file)
            )

    return files

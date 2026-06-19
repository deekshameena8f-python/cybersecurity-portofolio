from src.scanner import get_files
from src.hash_utils import calculate_hash


def check_integrity(directory, baseline):
    current = {}

    for file in get_files(directory):
        file_hash = calculate_hash(file)

        if file_hash:
            current[file] = file_hash

    return current

def detect_changes(current, baseline):

    modified = []

    for file in baseline:

        if file in current:

            if baseline[file] != current[file]:
                modified.append(file)

    return modified

def detect_new_files(current, baseline):

    new_files = []

    for file in current:

        if file not in baseline:
            new_files.append(file)

    return new_files

def detect_deleted_files(current, baseline):

    deleted = []

    for file in baseline:

        if file not in current:
            deleted.append(file)

    return deleted

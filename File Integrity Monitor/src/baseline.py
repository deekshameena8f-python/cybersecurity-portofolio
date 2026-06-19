import json

from src.hash_utils import calculate_hash
from src.scanner import get_files


def create_baseline(directory, output_file):
    baseline = {}

    files = get_files(directory)

    for file in files:
        file_hash = calculate_hash(file)

        if file_hash:
            baseline[file] = file_hash

    with open(output_file, "w") as f:
        json.dump(
            baseline,
            f,
            indent=4
        )

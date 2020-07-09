#!/usr/bin/env python

"""
Create a new file of specific size
"""

import os

FILE_SIZE_IN_KB = 1024 * 25
FILE_MAX_SIZE_IN_KB = 1024 * 25  # 10MB

if FILE_SIZE_IN_KB > FILE_MAX_SIZE_IN_KB:
    print(f"Required file size is greater than {FILE_MAX_SIZE_IN_KB}")
    exit(1)

script_dir_path = os.path.dirname(os.path.realpath(__file__))
TARGET_FOLDER = script_dir_path
TARGET_FILENAME = f"generated_file_{FILE_SIZE_IN_KB}.out"
TARGET_FILE = os.path.join(TARGET_FOLDER, TARGET_FILENAME)

with open(TARGET_FILE, 'w') as f:
    file_size_in_bytes = FILE_SIZE_IN_KB * 1024
    f.write('\0' * file_size_in_bytes)

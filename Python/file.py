import os
import shutil
from collections import defaultdict

def organize_files(source_folder):
    if not os.path.exists(source_folder):
        print("Source folder not found!")
        return()

    file_counts = defaultdict(int)
    total_moved = 0

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isdir(file_path):
            continue
        extension = os.path.splitext(filename)[1].lower()
        if extension:
            extension = extension[1:].upper()
        else:
            extension = "OTHERS"
        folder_path = os.path.join(source_folder, extension)
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(file_path, os.path.join(folder_path, filename))
        file_counts[extension] += 1
        total_moved += 1

    print(f"\n Total files organized: {total_moved}")
    print("Files moved into folders:\n")
    for ext,count in file_counts.items():
        print(f"   {ext}: {count} file(s)")
source_folder = r"C:\Users\teddy\Downloads"
organize_files(source_folder)

import os
from subprocess import call


def process_file(directory, f):
    # Error handling
    if len(f) < 3:
        return
    if f[-3:] == '.yc':
        print("Processing: " + directory + "/" + f)
        call(["youclid",
              # Input file
              directory + "/" + f,
              # Output flag
              "--output",
              # Output director, created from the current file path (without
              # the markup directory, and without the yc extension
              "./html/" + "/".join(directory.split("/")[1:]) + "/" + f[:-3],
              # --final flag
              "--final"])


def process_folder(path):
    for current_dir, directories, files in os.walk(path):
        for f in files:
            process_file(current_dir, f)
        for d in directories:
            process_folder(d)


if __name__ == "__main__":
    process_folder("markup")

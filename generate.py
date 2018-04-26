from subprocess import call, Popen, PIPE


def process_file(f):
    # Error handling
    if f[-3:] == '.yc':
        print("Processing: " + f)
        call(["youclid",
              # Input file
              f,
              # Output flag
              "--output",
              # Output director, created from the current file path (without
              # the markup directory, and without the yc extension
              "./html/" + "/".join(f.split("/")[1:])[:-3],
              # --final flag
              "--final"])


def get_changed():
    """Get all of the files that have changed
    Equivilent to the following command:
    git status *.yc | grep ".yc" | awk '{print $1}'
    """
    git = Popen(("git", "status", "*.yc"), stdout=PIPE)
    grep = Popen(("grep", ".yc"), stdin=git.stdout, stdout=PIPE)
    awk = Popen(("awk", "{print $1}"), stdin=grep.stdout, stdout=PIPE)
    files = awk.communicate()[0].decode("UTF-8").split("\n")

    git = Popen(("git", "status", "*.yc"), stdout=PIPE)
    grep = Popen(("grep", ".yc"), stdin=git.stdout, stdout=PIPE)
    awk = Popen(("awk", "{print $2}"), stdin=grep.stdout, stdout=PIPE)
    files += awk.communicate()[0].decode("UTF-8").split("\n")

    return files


if __name__ == "__main__":
    for f in get_changed():
        if f:
            process_file(f)

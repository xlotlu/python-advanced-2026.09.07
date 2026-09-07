import glob
import itertools
import time
from pathlib import Path
from multiprocessing.dummy import Pool as ThreadPool


def search_term(filename, term):
    with open(filename, "r") as f:
        try:
            for line in f:
                if term in line:
                    print(line, end="")
        except UnicodeDecodeError as ex:
            print(ex, filename)


def find_files(path, extension, /, *, recursive=False):
    pattern = Path(path)
    if recursive:
        pattern /= "**"
    pattern /= f"*.{extension}"
    return glob.iglob(str(pattern), recursive=recursive, include_hidden=True)


def search_across_files(root_path, file_extension, term):
    pool = ThreadPool(10)
    filenames = find_files(root_path, file_extension, recursive=True)
    result = pool.starmap(search_term, zip(filenames, itertools.repeat(term)))
    pool.close()
    pool.join()
    return result


if __name__ == "__main__":
    time_start = time.time()
    search_across_files("..", "py", "import")
    time_diff = time.time() - time_start
    print(f"Execution took {time_diff}s.")

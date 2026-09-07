import concurrent.futures
import glob
import time
from pathlib import Path


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
    for filename in find_files(root_path, file_extension, recursive=True):
        search_term(filename, term)


def search_across_files_concurrent(root_path, file_extension, term, Executor):
    futures = []
    with Executor(max_workers=10) as executor:
        for filename in find_files(root_path, file_extension, recursive=True):
            future = executor.submit(search_term, filename, term)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == "__main__":
    time_start = time.time()
    search_across_files("..", "py", "import")
    time_diff = time.time() - time_start
    print(f"Execution took {time_diff}s.")

    time_start = time.time()
    search_across_files_concurrent(
        "..", "py", "import",
        concurrent.futures.ProcessPoolExecutor)
    time_diff = time.time() - time_start
    print(f"Execution took (multiprocess) {time_diff}s.")

    time_start = time.time()
    search_across_files_concurrent(
        "..", "py", "import",
        concurrent.futures.ThreadPoolExecutor)
    time_diff = time.time() - time_start
    print(f"Execution took (multithread) {time_diff}s.")

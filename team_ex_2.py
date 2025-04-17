# Concurrency example using multiple implementations
# Example searches for a topic on Wikipedia, gets related topics,
# and saves the references from related topics into their own text files.
# wikipedia library info: https://thepythoncode.com/article/access-wikipedia-python
# concurrent.futures info: https://docs.python.org/3/library/concurrent.futures.html

import os
import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Directory to store downloaded reference files
WIKI_DIR = "wiki_dl"

# Convert objects produced by the wikipedia package to string for saving to text file
def convert_to_str(obj):
    if isinstance(obj, list):
        return '\n'.join(obj)
    return str(obj)

# Ensure the output directory exists
def ensure_directory():
    if not os.path.exists(WIKI_DIR):
        os.makedirs(WIKI_DIR)

# Shared download and save function for all implementations
def dl_and_save(item):
    try:
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        out_filename = os.path.join(WIKI_DIR, f"{title}.txt")
        print(f'Writing to {out_filename}')
        with open(out_filename, 'w', encoding='utf-8') as fileobj:
            fileobj.write(references)
    except Exception as e:
        print(f"Failed to download {item}: {e}")

# IMPLEMENTATION 1: Sequential execution
def wiki_sequentially(search_term):
    print('\nSequential Execution:')
    ensure_directory()
    t_start = time.perf_counter()

    results = wikipedia.search(search_term)
    for item in results:
        dl_and_save(item)

    t_lapse = time.perf_counter() - t_start
    print(f'Code executed in {t_lapse:.2f} seconds')

# IMPLEMENTATION 2: Concurrent execution with threads
def concurrent_threads(search_term):
    print('\nThread Pool Execution:')
    ensure_directory()
    t_start = time.perf_counter()

    results = wikipedia.search(search_term)
    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save, results)

    t_lapse = time.perf_counter() - t_start
    print(f'Code executed in {t_lapse:.2f} seconds')

# IMPLEMENTATION 3: Concurrent execution with processes
def concurrent_process(search_term):
    print('\nProcess Pool Execution:')
    ensure_directory()
    t_start = time.perf_counter()

    results = wikipedia.search(search_term)
    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save, results)

    t_lapse = time.perf_counter() - t_start
    print(f'Code executed in {t_lapse:.2f} seconds')

# Main execution block
if __name__ == "__main__":
    user_input = input("Enter Wikipedia search term: ").strip()
    search_term = user_input if len(user_input) >= 4 else "generative artificial intelligence"

    wiki_sequentially(search_term)
    concurrent_threads(search_term)
    concurrent_process(search_term)


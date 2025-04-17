# Team Exercise #2 – Wikipedia Concurrency Downloader

## Overview
This Python script explores three different implementations for downloading Wikipedia references related to a search term. It uses the `wikipedia` and `concurrent.futures` libraries to:

- Search for related topics
- Download references for each topic
- Save each topic's references in a separate `.txt` file

---

## Features

### 1. User Input Support
- The program prompts the user to input a Wikipedia search term.
- If the input is fewer than 4 characters, it defaults to **"generative artificial intelligence"**.

### 2. Organized File Storage
- All reference files are saved in a dedicated directory named **`wiki_dl/`**.

### 3. Three Execution Modes
- **Sequential:** Each topic is processed one after another.
- **Thread Pool:** Concurrent execution using multiple threads.
- **Process Pool:** Concurrent execution using multiple processes.

### 4. Robust Exception Handling
- The download logic handles exceptions gracefully, allowing the script to continue even if a page fails to download.

---

## Issues Addressed

| Issue # | Description                      | Resolution                            |
|---------|----------------------------------|----------------------------------------|
| 1       | Hardcoded search term            | Added input prompt with fallback logic |
| 2       | No output directory              | Implemented `ensure_directory()`       |
| 3       | Repeated download logic          | Centralized into `dl_and_save()`       |
| 4       | No error handling                | Wrapped download logic in try/except   |

---

## Code Structure

```plaintext
├── team_ex_2.py
├── team_ex_2.md
└── wiki_dl/
    ├── Topic1.txt
    ├── Topic2.txt
    └── ...
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install wikipedia
```

### 2. Execute the Script
```bash
python team_ex_2.py
```

### 3. Provide a Search Term
When prompted, enter a topic to search. If your input is fewer than 4 characters, the default "generative artificial intelligence" will be used.

---



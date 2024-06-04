# PDF Compression for ML Conference Submissions

This repository provides a Python-based solution to compress PDF files to meet the file size requirements of top-tier ML conferences. These venues often require that the size of the submitted papers does not exceed 10MB. This script uses Ghostscript to compress PDF files efficiently.

## Features

- Compress individual PDF files.
- Compress all PDF files in a specified directory.
- Replace original files with compressed versions automatically.

## Requirements

- Python 3.x
- Ghostscript

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/MingyuKim87/pdf-compression.git
    cd pdf-compression
    ```

2. **Install Ghostscript:**

    - **Ubuntu/Debian:**
        ```bash
        sudo apt-get install ghostscript
        ```

    - **macOS (using Homebrew):**
        ```bash
        brew install ghostscript
        ```

    - **Windows:**
        Download and install Ghostscript from [here](https://www.ghostscript.com/download.html).

## Usage

### Compress a Single PDF File

To compress a single PDF file, you can use the `compress_pdf` function directly. Example:

```python
from pdf_compression import compress_pdf

input_file_path = 'path/to/your/input.pdf'
output_file_path = 'path/to/your/output.pdf'
compress_pdf(input_file_path, output_file_path)

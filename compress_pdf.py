import os
import subprocess

def compress_pdf(input_file_path, output_file_path):
    try:
        # Call Ghostscript to compress the PDF
        command = [
            'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
            '-dPDFSETTINGS=/printer',  # Options: /screen, /ebook, /printer, /prepress, /default
            '-dNOPAUSE', '-dQUIET', '-dBATCH',
            f'-sOutputFile={output_file_path}', input_file_path
        ]
        subprocess.run(command, check=True)
        print(f"Compressed {input_file_path} and saved as {output_file_path}")
    except Exception as e:
        print(f"Failed to compress {input_file_path}: {e}")

def compress_all_pdfs_in_directory(directory_path):
    # Verify the directory path
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist or is not a directory.")
        return
    
    # Iterate over all files and subdirectories in the directory
    for root, dirs, files in os.walk(directory_path):
        print(f"Traversing directory: {root}")
        for file_name in files:
            print(f"Found file: {file_name}")
            if file_name.lower().endswith('.pdf'):
                input_file_path = os.path.join(root, file_name)
                output_file_path = os.path.join(root, f"compressed_{file_name}")
                compress_pdf(input_file_path, output_file_path)
                
                # Replace the original file with the compressed file
                os.replace(output_file_path, input_file_path)
                print(f"Replaced original file with compressed file: {input_file_path}")

# Define the directory containing the PDF files
directory_path = os.path.join(os.getcwd(), 'Figures')

# Compress all PDFs in the directory
compress_all_pdfs_in_directory(directory_path)
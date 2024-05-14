# FilesToBinary

## Description
FilesToBinary is a Python script that converts files (DOCX and PDF) to binary format and stores them in a MongoDB database.

## Installation
1. Clone the repository: git clone https://github.com/NikKnez/filesToBinary.git
2. Install the required libraries: `pip install pymongo PyPDF2`
3. Adjust the file paths and MongoDB connection details in the script to match your environment.

## Usage
1. Ensure that MongoDB is running.
2. Run the script: python filesToBinary.py


## File Types Supported
- **DOCX**: Microsoft Word Document
- **PDF**: Portable Document Format

## Dependencies
- **pymongo**: Python driver for MongoDB.
- **PyPDF2**: Library for reading and manipulating PDF files.

## Configuration
- `docx_file_path`: Path to the DOCX file you want to convert.
- `pdf_file_path`: Path to the PDF file you want to convert.
- `mongo_uri`: MongoDB connection URI.
- `database_name`: Name of the MongoDB database.
- `collection_name`: Name of the MongoDB collection.

## Notes
- Ensure that the specified file paths exist and are accessible.
- MongoDB must be installed and running to store the binary data.
- This script is designed to work with default MongoDB settings. Adjustments may be needed for non-default configurations.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any enhancements or bug fixes.


**Developed by [NikKnez](https://github.com/NikKnez)**


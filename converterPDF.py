# Import necessary libraries
from pymongo import MongoClient
import os
import PyPDF2

# Define the file path to the PDF file
pdf_file_path = r'C:\path\to\your\file.pdf'

# MongoDB connection details (default)
mongo_uri = 'mongodb://localhost:27017/'

# Database and collection names
database_name = 'your_db_name'
collection_name = 'your_db_collection'

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# Check if the file exists
if not os.path.exists(pdf_file_path):
    print(f"File not found: {pdf_file_path}")
else:
    # Open the PDF file in binary mode
    with open(pdf_file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to store text content
        text_content = ''

        # Iterate through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text_content += page.extract_text()

        # Convert text content to binary data
        binary_data = text_content.encode()

        # Create a document for the file
        doc = {
            'filename': os.path.basename(pdf_file_path),  # File name
            'filetype': 'application/pdf',  # File type
            'content': binary_data  # Binary content
        }

        # Insert the document into MongoDB
        result = collection.insert_one(doc)

        # Print the ID of the inserted document
        print(f"File inserted with ID: {result.inserted_id}")

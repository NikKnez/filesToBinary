# Import necessary libraries
from pymongo import MongoClient
import os

# Define the file path to the DOCX file
# Adjust the file path to the location of your DOCX file
docx_file_path = r'C:\path\to\your\file.docx'

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
if not os.path.exists(docx_file_path):
    print(f"File not found: {docx_file_path}")
else:
    # Open the DOCX file in binary mode
    with open(docx_file_path, 'rb') as file:
        # Read the file's binary data
        binary_data = file.read()

        # Create a document for the file
        doc = {
            'filename': os.path.basename(docx_file_path),  # File name
            'filetype': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',  # File type
            'content': binary_data  # Binary content
        }

        # Insert the document into MongoDB
        result = collection.insert_one(doc)

        # Print the ID of the inserted document
        print(f"File inserted with ID: {result.inserted_id}")

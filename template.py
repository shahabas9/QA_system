from pathlib import Path
import os

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files =[
    'QAwithpdf/__init__.py',
    'QAwithpdf/data_ingestion.py',
    'QAwithpdf/embedding.py',
    'QAwithpdf/model.py',
    'StreamlitApp.py',
    'logger.py',
    'exception.py',
    'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    
    else:
        logging.info(f"{filename} is already created")
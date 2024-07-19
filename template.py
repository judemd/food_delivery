import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter the name of the project: ")
    if project_name != "":
        break

# src/__init__.py
# src/components/__init__.py
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components__init__.py",
    f"{project_name}/config__init__.py",
    f"{project_name}/constants__init__.py",
    f"{project_name}/entity__init__.py",
    f"{project_name}/exception__init__.py",
    f"{project_name}/logger__init__.py",
    f"{project_name}/pipeline__init__.py",
    f"{project_name}/utils__init__.py",
    f"{project_name}/components__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "log.py",
    "exceptions.py",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"File {filepath} already exists.")


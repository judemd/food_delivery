# from setuptools import setup, find_packages
# from typing import List

# PROJECT_NAME = 'Machine Learning Project',
# VERSION = '0.0.1',
# DESCRIPTION = 'Modular Machine Learning Coding',
# AUTHOR_NAME = 'Jude Dass',
# AUTHOR_EMAIL = 'jgblr18@gmail.com'
# REQUIREMENTS_FILE_NAME = 'requirements.txt'
# HYPHEN_E_DOT = "-e ."

# # Open requirements.txt file
# # Read
# # \n ""
# def get_requirements_list() -> List[str]:
#     with open(REQUIREMENTS_FILE_NAME) as requirements_file:
#         requirements_list = requirements_file.readlines()
#         requirements_list = [requirement_name.replace("\n","") for requirement_name in requirements_list]
        
#         if HYPHEN_E_DOT in requirements_list:
#             requirements_list.remove(HYPHEN_E_DOT)
#         return requirements_list

# setup(name=PROJECT_NAME,
#       version=VERSION,
#       description=DESCRIPTION,
#       author=AUTHOR_NAME,
#       author_email=AUTHOR_EMAIL,
#       packages=find_packages(),
#       install_requires = get_requirements_list()
#      )

from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Machine Learning Project'
VERSION = '0.0.1'
DESCRIPTION = 'Modular Machine Learning Coding'
AUTHOR_NAME = 'Jude Dass'
AUTHOR_EMAIL = 'jgblr18@gmail.com'
REQUIREMENTS_FILE_NAME = 'requirements.txt'

# Read the requirements from the file
def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()
        # Remove any trailing newlines and handle -e . if present
        requirements_list = [req.strip() for req in requirements_list]
        if "-e ." in requirements_list:
            requirements_list.remove("-e .")
        return requirements_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "Python Files"
LONG_DESCRIPTION = "This package contains Python functions and modules for analyst test task."

# Reading requirements from the requirements.txt file (optional)
# with open('requirements.txt') as f:
#     required = f.read().splitlines()

# Setting up
setup(
    name="test-data-analyst-task",
    version=VERSION,
    author="Anna Konkina",
    author_email="annakonkina3998@yandex.ru",  # Make sure to replace with actual email
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",  # You can also use "text/markdown" if your README is in Markdown format
    url="https://github.com/annakonkina/test-data-analyst-task",  # GitHub URL or your repo URL
    packages=find_packages(),  # Automatically find packages in the repo
    install_requires=["ipython==7.34.0"],  # List of dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change to your actual license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the required Python version
)
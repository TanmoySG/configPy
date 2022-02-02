import json
import sys
from setuptools import setup, find_packages, Command

repository = ""

if "--pypi" in sys.argv:
    repository = "pypi"
    sys.argv.remove("--pypi")

if "--test-pypi" in sys.argv:
    repository = "test-pypi"
    sys.argv.remove("--test-pypi")

with open("documentation.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def getVersion(repo)->str:
    with open("./utilities/version.json", "r") as verFile:
        versions = json.load(verFile)

    return versions[repo]

setup(
    name='configParsePy',
    version=getVersion(repository),
    author='Tanmoy Sen Gupta',
    author_email='tanmoysps@gmail.com',
    url='https://github.com/TanmoySG/configPy',
    description='A tiny Configuration File Parser for Python Projects. Currently Supports JSON files only.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    keywords=['imports', 'configurations', 'python', 'project'],
    install_requires=[],
    zip_safe=False
)

'''
[Usage]

python setup.py sdist bdist_wheel [--test-pypi / --pypi]

'''

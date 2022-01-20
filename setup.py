from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='configParsePy',
    version='0.0.8',
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
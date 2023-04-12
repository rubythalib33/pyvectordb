import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvectordb",
    version="0.1.0",
    author="Ruby Abdullah",
    author_email="rubyabdullah14@gmail.com",
    description="A library for working with a vector database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rubythalib33/pyvectordb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

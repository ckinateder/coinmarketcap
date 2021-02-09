import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coinmarketcap",  # Replace with your own username
    version="0.0.1",
    author="Calvin Kinateder",
    author_email="calvinkinateder@gmail.com",
    description="A custom API wrapper for coinmarketcap.com to avoid paying $79 a month for access",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mal-api",
    version="0.5.1",
    description="A local MyAnimeList API ",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daren Liang",
    author_email="darenliang@outlook.com",
    url="https://github.com/darenliang/mal-api",
    packages=setuptools.find_packages(),
    install_requires=["requests", "beautifulsoup4"],
    keywords=["api", "myanimelist"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

import setuptools

with open("PYPI_README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="decohints",
    version="1.0.2",
    author="Grigoriy Gusev",
    author_email="thegrigus@gmail.com",
    description="A decorator for decorators that allows you to see the parameters of a decorated function when using it in PyCharm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gri-gus/decohints",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

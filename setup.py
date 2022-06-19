import setuptools

VERSION = "1.0.5"

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="decohints",
    version=VERSION,
    author="Grigoriy Gusev",
    author_email="thegrigus@gmail.com",
    description="A decorator for decorators that allows you to see the parameters of a decorated function when using it in PyCharm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gri-gus/decohints",
    packages=setuptools.find_packages(),
    package_data={"decohints": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    license="Apache Software License",
    keywords=[
        "python",
        "decorator",
        "deco",
        "decohints",
        "hints",
        "decor",
        "decohint",
        "python-decorator",
        "helper",
        "util"
    ]
)

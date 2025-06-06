import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="Topsis-Adrija-102203509",
    version="1.0.3",
    description="Topsis Package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/adrija26sg/topsis_assgn1",
    author="Adrija Sengupta",
    author_email="adrija26sg@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=['numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'topsis = topsis.__main__:main',
        ],
    },
    python_requires=">=3.6",
)
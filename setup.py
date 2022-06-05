import setuptools
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setuptools.setup(
    name="fastvalidate",
    version="0.0.4",
    url="https://github.com/mojtabaahn/fast-validate",
    author="Mojtabaa Habibain",
    author_email="mojtabaa.hn@gmail.com",
    description="Easy validation for python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
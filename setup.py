import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

packages = ['hpcomt']

requires = [
    'platform'
]

setuptools.setup(
    name="hpcomt",
    version="0.1.1",
    author="Sudhanshu Patil",    
    description="Detect OS Name, E.g. 'Android', 'Linux', 'Windows' or 'Java' , Etc. Specially For Android",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidhu-patil/hpcomt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 

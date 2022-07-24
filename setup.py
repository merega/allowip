import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="allowip",
    version="0.2",
    author="Alexandr Chamran",
    author_email="chamran.merega@gmail.com",
    description="Authorized IP management.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="package_github_page",
    packages=['allowip'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

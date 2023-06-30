import setuptools
setuptools.setup(
    name="mr",
    version="1.0.0",
    author="linrol",
    author_email="linrolmail@gmail.com",
    description="create merge request",
    install_requires=['requests'],
    long_description=open("README.md", 'r').read(),
    long_description_content_type="text/markdown",
    url="[https://github.com/linrol/mr](https://github.com/linrol/mr)",
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
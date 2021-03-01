#!/usr/bin/env python

import re
import setuptools

version = "1.0.2"
long_description ="this package is  send wx message to your phone "
# with open('wxmpy/__init__.py', 'r') as fd:
#     version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
#                         fd.read(), re.MULTILINE).group(1)

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="wxmpy",
    version=version,
    author="rehylas",
    author_email="rehylas@sina.com",
    description="send wx message  to my phone.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/rehylas/wxmpy",
    install_requires=[
        # 'requests!=2.9.0',
    ],
    packages=setuptools.find_packages(exclude=("test")),
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ),
    exclude_package_data={'': ["wxmpy/test.py", "wxmpy/config.txt"]},
)
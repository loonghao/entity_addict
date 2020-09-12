"""This setup script packages entity_addict."""

# Import third-party modules
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# Import local modules
import entity_addict

setup(
    name="entity_addict",
    version=entity_addict.__version__,
    packages=find_packages(),
    url="https://github.com/loonghao/entity_addict",
    license="MIT",
    author="Long Hao",
    author_email="hal.long@outlook.com",
    description="An extended version of addict.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "addict>=2.0",
    ],
)

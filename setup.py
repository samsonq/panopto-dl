#!/usr/bin/env python3
from setuptools import setup, find_packages
import pip
import logging
import pkg_resources
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution('pip').version
    pip_version = list(map(int, pip_ver.split('.')[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path,
                                         session=pip.download.PipSession())
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]


try:
    install_reqs = _parse_requirements("requirements.txt")
except Exception as e:
    logging.warning('Fail load requirements file, so using default ones.')
    install_reqs = []

setup(
    name="panopto_dl",
    version="0.1.1",
    author="Samson Qian",
    author_email="samsonqian@gmail.com",
    packages=["panopto_dl", "panopto_dl.PanoptoDownloader"],
    url="https://github.com/samsonq/panopto-dl",
    license="MIT",
    description="Download video from Panopto",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=install_reqs,
    python_requires=">=3.7",
    keywords="panopto download video",
)

from setuptools import setup, find_packages
 
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.9.6"
]
 
setup(
  name="pastebinapi",
  version="0.0.1",
  description="This module allows to use Pastebin API very easily.",
  long_description=open("README.md").read(),
  url="https://github.com/venaxyt/pastebinapi",  
  author="Venax",
  author_email="venaxumofficial@gmail.com",
  license="MIT", 
  classifiers=classifiers,
  keywords="pastebin", 
  install_requires=["requests"] 
)

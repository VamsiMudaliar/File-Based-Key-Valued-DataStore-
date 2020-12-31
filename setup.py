from setuptools import setup,find_packages


with open("README.md") as fh:
	long_description= fh.read()


setup(name="LocalDataStore",
version="1.5.1",
description="A File Based DataStore",
author="A Vamsi Mudaliar",
author_email="vamsimudaliar@gmail.com",
long_description=long_description,
long_description_content_type="text/markdown",
license='MIT',
packages=find_packages(),
install_requires=[],
classifiers=[
"Development Status :: 5 - Production/Stable",
"Intended Audience :: Education",
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires=">=3.6",
zip_safe=False,
)
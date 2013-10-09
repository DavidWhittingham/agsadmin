from ez_setup import use_setuptools
use_setuptools()
    
import agsadmin

from setuptools import setup, find_packages
setup(
    name = "agsadmin",
    version = agsadmin.__version__,
    packages = find_packages(),
    
    #dependencies
    install_requires = [
        "rsa>=3.1.1",
        "requests>=1.2.0"
    ],
    
    #misc files to include
    package_data = {
        "": ["LICENSE"]
    },
    
    #PyPI MetaData
    author = agsadmin.__author__,
    description = "ArcGIS Server REST Admin API Proxy",
    license = "BSD 3-Clause",
    keywords = "arcgis esri",
    url = "https://github.com/DavidWhittingham/agstools",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7"
    ),
    
    zip_safe = True
)

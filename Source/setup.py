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
        "": ["license.txt", "authors.txt"]
    },
    
    #PyPI MetaData
    author = agsadmin.__author__,
    description = "ArcGIS Server REST Admin API Proxy",
    license = "BSD 3-Clause",
    keywords = "arcgis esri",
    
    zip_safe = True
)
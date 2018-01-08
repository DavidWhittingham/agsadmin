try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('agsadmin/_version.py') as fin: exec(fin)

packages = [
    "agsadmin",
    "agsadmin.exceptions",
    "agsadmin.services",
    "agsadmin.machines"
]
	
setup(
    name = "agsadmin",
    version = __version__,
    packages = packages,
    
    #dependencies
    install_requires = [
        "python-dateutil>=2.5.3",
        "rsa>=3.1.1",
        "requests>=1.2.0"
    ],
    
    #misc files to include
    package_data = {
        "": ["LICENSE"]
    },
    
    #PyPI MetaData
    author = __author__,
    description = "ArcGIS Server REST Admin API Proxy",
    license = "BSD 3-Clause",
    keywords = "arcgis esri",
    url = "https://github.com/DavidWhittingham/agsadmin",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7"
    ),
    
    zip_safe = False
)

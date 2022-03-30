import os
from pie import *

# Get OS-specific partial path
VENV_BUILD = os.path.join(".venvs", "build")
VENV_TEST = os.path.join(".venvs", "test")

@task
def build():
    with venv(VENV_BUILD):
        cmd(r"python setup.py bdist_wheel clean --all")


@task
def createVenvs():
    venv(VENV_BUILD).create()
    venv(VENV_TEST).create()


@task
def setup():
    createVenvs()
    updatePackages()


@task
def test():
    with venv(VENV_TEST):
        cmd(r"python -m pytest -s --cov-report term --cov-report html --cov=agsadmin .\\tests")


@task
def updatePackages():
    with venv(VENV_BUILD):
        pip(r"install -U setuptools")
        pip(r"install -U pip")
        pip(r"install -U -r requirements.build.txt")
        pip(r"install -U -r requirements.txt")

    with venv(VENV_TEST):
        pip(r"install -U setuptools")
        pip(r"install -U pip")
        pip(r"install -U -r requirements.test.txt")
        pip(r"install -U -r requirements.txt")


@task([OptionsParameter('version')])
def upload(version):
    with venv(VENV_BUILD):
        cmd(r'python -m twine upload dist\agsadmin-{}-py2.py3-none-any.whl'.format(version))
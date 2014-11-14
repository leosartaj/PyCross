try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def readFile(fName):
    with open(fName) as f:
        lines = f.read()
    return lines

setup(
    name = 'PyCross',
    version = '0.0.1',
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Single Player Tic-Tac-Toe game'),
    long_description = readFile('README.md'),
    license = 'MIT',
    keywords = 'game tic-tac-toe tictactoe play',
    url = 'http://github.com/leosartaj/PyCross',
    packages=['PyCross', 'PyCross/gui', 'PyCross/gui', 'PyCross/gui/svg'],
    package_data={'PyCross/gui/svg': ['*.svg'], 'PyCross/gui': ['*.glade']},
    scripts=['bin/pycross'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)

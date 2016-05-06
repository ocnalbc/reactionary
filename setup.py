from setuptools import setup

setup(
    name='reactionary',
    version='0.1',
    packages=['reactionary',],
    url='',
    license='GNU GPL V3',
    description='A reworking of isreactionary_bot',
    long_description=open('README.md').read(),
    author='me',
    install_requires=[
        'praw',
        'yaml',
    ],
    entry_points = {
        'console_scripts': ['react-cli=reactionary.command'],
    },
)

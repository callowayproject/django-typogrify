import os
from setuptools import setup, find_packages

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

setup(name='typogrify',
      version='1.1',
      description='Typography related template filters for Django applications',
      author='Christian Metts',
      author_email='xian@mintchaos.com',
      url='http://code.google.com/p/typogrify/',
      packages=['typogrify', 'typogrify.templatetags'],
      classifiers=['Development Status :: 1',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers :: Designers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      install_package_data=True,
      install_requires=read_file('requirements.txt'),
)

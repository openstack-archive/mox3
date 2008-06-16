#!/usr/bin/python2.4
from distutils.core import setup
# TODO(glasser): Make sure that test stuff is included/documented.
setup(name='mox',
      version='1.0.0',
      py_modules=['mox', 'stubout'],
      url='http://code.google.com/p/pymox/',
      maintainer='pymox maintainers',
      maintainer_email='mox-discuss@googlegroups.com',
      license='Apache License, Version 2.0',
      description='Mock object framework',
      long_description='''Mox is a mock object framework for Python based on the
Java mock object framework EasyMock.''',
      )

Mox3 - Mock object framework for Python 3.

Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

Use at your own risk ;) 

To install:

  $ python setup.py install

To run Mox3 internal tests you should download python-nose package and execute
(in mox3 directory):

  $ nosetests
  
The basic usage of mox3 is the same as with mox, but the initial import should
be made from the mox3 module:

  from mox3 import mox

To learn how to use mox3 you may check the documentation of the original mox
framework:

  http://code.google.com/p/pymox/wiki/MoxDocumentation

--

Mox is Copyright 2008 Google Inc, and licensed under the Apache
License, Version 2.0; see the file COPYING for details.  If you would
like to help us improve Mox, join the group.

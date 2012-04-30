# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# 
# This is a fork of the pymox library intended to work with Python 3.
# The file was modified by quermit@gmail.com and dawid.fatyga@gmail.com

from distutils.core import setup

setup(name='mox3',
      version='0.6.0',
      packages=['mox3', 'mox3.tests'],
      url='https://github.com/quermit/pymox',
      maintainer='quermit',
      maintainer_email='quermit@gmail.com',
      license='Apache License, Version 2.0',
      description='Mock object framework for Python 3',
      long_description=('Mox3 is an unofficial port of the of the mox '
                        'framework to Python 3. The library was tested on '
                        'Python version 3.2, 2.7 and 2.6.'),
      classifiers=['Programming Language :: Python',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Operating System :: OS Independent',
                   'Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Testing'],
      )

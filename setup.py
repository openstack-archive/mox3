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

setup(name='mox',
      version='0.5.4',
      py_modules=['mox', 'stubout'],
      url='https://github.com/quermit/pymox',
      maintainer='quermit',
      maintainer_email='quermit@gmail.com',
      license='Apache License, Version 2.0',
      description='Mock object framework',
      long_description=('Mox is a mock object framework for Python based on '
                        'the Java mock object framework EasyMock.'),
      )

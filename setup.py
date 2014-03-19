#!/usr/bin/env python

from distutils.core import setup

import version


setup(name='application_repository.jsonrpc',
      version=version.getVersion(),
      description='A json-rpc package which implements JSON-RPC over HTTP.',
      keywords='JSON RPC',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='https://github.com/wheeler-microfluidics/application_repository.jsonrpc',
      license='LGPL',
      packages=['jsonrpc'])

from setuptools import setup, find_packages
import os

version = 'dev'

setup(name='mk.recipe.modwsgi',
      version=version,
      description='WSGI from buildout',
      long_description=open('README.rst').read(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Buildout :: Recipe',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ],
      keywords='wsgi buildout',
      author='Kamal Mustafa',
      author_email='kamal.mustafa@gmail.com',
      url='https://github.com/k4ml/mk.recipe.modwsgi',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mk', 'mk.recipe'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'zc.recipe.egg',
      ],
      entry_points='''
      [zc.buildout]
      default = mk.recipe.modwsgi:Recipe
      ''',
      )

from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='werateit',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "logbook",
        "werkzeug",
        "routes",
        "pymongo",
        "quantumcore.storages",
        "quantumcore.exceptions",
            
      ],
      entry_points="""
        [paste.app_factory]
        backend = werateit.http.main:backend_factory
      """,
      )

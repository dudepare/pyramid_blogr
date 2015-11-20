import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid==1.5.7',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy==1.0.9',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms==2.0.2',
    'webhelpers2==2.0',
    'paginate==0.5',
    'paginate_sqlalchemy==0.2.0',
    ]

setup(name='pyramid_blogr',
      version='0.0',
      description='pyramid_blogr',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_blogr',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory] 
      main = pyramid_blogr:main
      [console_scripts]
      initialize_pyramid_blogr_db = pyramid_blogr.scripts.initializedb:main
      """,
      )

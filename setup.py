from setuptools import setup

version = '0.7.0'

setup(
  name = 'ravenclient',
  py_modules = ['ravenclient'],
  install_requires = ['beautifulsoup4 >= 4.3.0', 'requests >= 2.7.0'],
  version = version,
  description = 'A python requests adapter to automatically login to the Cambridge University Raven Login',
  author = 'Eric Wieser',
  author_email = 'wieser.eric+raven@gmail.com',
  url = 'https://github.com/eric-wieser/raven-client',
  download_url = 'https://github.com/eric-wieser/raven-client/tarball/v'+version,
  keywords = ['authentication', 'requests', 'raven'],
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Intended Audience :: Developers'
  ],
  test_suite='nose.collector',
  tests_require=['nose']
)

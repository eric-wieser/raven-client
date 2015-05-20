from distutils.core import setup
setup(
  name = 'ravenclient',
  py_modules = ['ravenclient'],
  install_requires = ['beautifulsoup4 >= 4.3'],
  version = '0.4',
  description = 'A python requests adapter to automatically login to the Cambridge University Raven Login',
  author = 'Eric Wieser',
  author_email = 'wieser.eric+raven@gmail.com',
  url = 'https://github.com/eric-wieser/raven-client',
  download_url = 'https://github.com/eric-wieser/raven-client/tarball/0.4',
  keywords = ['authentication', 'requests', 'raven'],
  classifiers = [],
)
from distutils.core import setup
setup(
  name = 'ravenclient',
  py_modules = ['ravenclient'],
  version = '0.3',
  description = 'A python requests adapter to automatically login to the Cambridge University Raven Login',
  author = 'Eric Wieser',
  author_email = 'wieser.eric@gmail.com',
  url = 'https://github.com/eric-wieser/raven-client',
  download_url = 'https://github.com/eric-wieser/raven-client/tarball/0.3',
  keywords = ['authentication', 'requests', 'raven'],
  classifiers = [],
)
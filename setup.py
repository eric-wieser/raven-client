from distutils.core import setup
setup(
  name = 'ravenclient',
  py_modules = ['ravenclient'],
  version = '0.2',
  description = 'A python requests adapter to automatically login to the Cambridge University Raven Login',
  author = 'Eric Wieser',
  author_email = 'wieser.eric@gmail.com',
  url = 'https://github.com/eric-wieser/raven-client', # use the URL to the github repo
  download_url = 'https://github.com/eric-wieser/raven-client/tarball/0.1', # I'll explain this in a second
  keywords = ['authentication', 'requests', 'raven'], # arbitrary keywords
  classifiers = [],
)
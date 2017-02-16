import unittest
import os
import getpass

import ravenclient
import requests
from bs4 import BeautifulSoup

CRSID = os.environ.get('CRSID')
if CRSID:
	PASSWORD = getpass.getpass("Enter password for {}: ".format(CRSID))

class RavenTests(unittest.TestCase):
	@unittest.skipIf(not CRSID, reason='no auth data present on command line')
	def test_working(self):
		with requests.Session() as s:
			s.mount(ravenclient.auth_url, ravenclient.HTTPAdapter(CRSID, PASSWORD))

			r = s.get('http://www3.eng.cam.ac.uk/exams/results/2012/pt1a.html')

			s = BeautifulSoup(r.text, 'lxml')
			self.assertTrue('raven' not in s.find('title').text.lower())

	def test_bad_password(self):
		with requests.Session() as s:
			s.mount(ravenclient.auth_url, ravenclient.HTTPAdapter('efw27', 'not my password'))

			with self.assertRaises(ravenclient.CredentialError):
				r = s.get('http://www3.eng.cam.ac.uk/exams/results/2012/pt1a.html')

if __name__ == '__main__':
	unittest.main(buffer=False)

.. _requests: http://docs.python-requests.org/en/latest/

raven-client
============

A requests_ adapter to automatically login to the Cambridge University Raven Login

Example usage:

.. code-block:: python

  import ravenclient
  import requests

  s = requests.Session()
  s.mount(ravenclient.auth_url, ravenclient.HTTPAdapter('efw27', 'mypassword'))

  r = s.get('http://www3.eng.cam.ac.uk/exams/results/2012/pt1a.html')

  print r.text[:600]

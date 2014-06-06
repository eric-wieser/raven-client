raven-client
============

A [`requests`](http://docs.python-requests.org/en/latest/) adapter to automatically login to the Cambridge University Raven Login

Example usage:

```python

import raven
import requests

s = requests.Session()
s.mount(raven.auth_url, raven.HTTPAdapter('efw27', 'mypassword'))


r = s.get('http://www3.eng.cam.ac.uk/exams/results/2012/pt1a.html')

print r.text[:600]
```

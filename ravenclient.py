#! python2
from bs4 import BeautifulSoup as soup
import requests

auth_url = 'https://raven.cam.ac.uk/auth/'

class HTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, username, password, **kwargs):
        super(HTTPAdapter, self).__init__(**kwargs)

        self.userid = username
        self.pwd = password

    def send(self, request, **kwargs):
        response = super(HTTPAdapter, self).send(request, **kwargs)

        if response.url.startswith(auth_url + u'authenticate.html'):
            form = soup(response.text).find('form')
            data = {
                i['name']: i.attrs.get('value')
                for i in form.find_all('input')
                if i['type'] not in ('checkbox', 'radio', 'submit')
            }
            data['userid'] = self.userid
            data['pwd'] = self.pwd

            auth_request = requests.Request('POST', auth_url + 'authenticate2.html', data=data)
            auth_request = auth_request.prepare()

            response = super(HTTPAdapter, self).send(auth_request)

        return response

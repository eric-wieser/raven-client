#! python2
from bs4 import BeautifulSoup as soup
import requests


auth_url = 'https://raven.cam.ac.uk/auth/'


class AuthError(IOError):
    """
    Raised if the library cannot parse the login form. See the .reponse
    attribute to debug
    """
    def __init__(self, message, response):
        super(AuthError, self).__init__(message, response)
        self.response = response


class HTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, username, password, **kwargs):
        super(HTTPAdapter, self).__init__(**kwargs)

        self.userid = username
        self.pwd = password

    def send(self, request, **kwargs):
        response = super(HTTPAdapter, self).send(request, **kwargs)

        # ignore redirects
        if 'location' in response.headers:
            pass

        # look for the login page url
        elif response.url.startswith(auth_url + u'authenticate.html'):
            form = soup(response.text).find('form')
            if not form:
                raise AuthError("Could not parse login form", response)

            # build the login form param dict
            data = {
                i['name']: i.attrs.get('value')
                for i in form.find_all('input')
                if i['type'] not in ('checkbox', 'radio', 'submit')
            }
            data['userid'] = self.userid
            data['pwd'] = self.pwd

            # make a second request
            auth_request = requests.Request('POST', auth_url + 'authenticate2.html', data=data)
            auth_request = auth_request.prepare()

            response = super(HTTPAdapter, self).send(auth_request)

        return response

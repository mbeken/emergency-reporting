import requests
import re
import datetime
from urllib.parse import urljoin
from .util import BASE_URL, AUTH_URL
from .excpetion import AuthException
import logging


class Token():

    def __init__(self, access_token, life, received_at):
        self.access_token = access_token
        # self.refresh_token = refresh_token
        self.life = life
        self.recevied_at = received_at

    def age(self):
        age = datetime.datetime.utcnow() - self.recevied_at
        print(age.seconds)
        return age.seconds

    def token_too_old(self):
        if self.age() > (self.life * 0.9):
            return True
        else:
            return False


class Auth():

    def __init__(self, client_id, client_secret, username, password, er_aid, er_uid):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.er_aid = er_aid
        self.er_uid = er_uid
        self.base_url = BASE_URL
        self.code = None
        self.token = None
        self.primary_key = None

    def _get_auth_code(self):
        path = 'auth/Authorize.php'
        data = {
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id,
            "response_type": "code",
            "state": "xyz"
        }
        headers = {
            'Ocp-Apim-Subscription-Key': self.primary_key
        }
        r = requests.post(urljoin(self.base_url, path), data=data, headers=headers)
        if r.ok:
            try:
                self.code = re.search(b'code=(.*)&', r.content).group(1)
            except AttributeError:
                logging.error(r.content)
                logging.error(str(r.status_code))                
                raise AuthException
        else:
            logging.error(r.content)
            logging.error(str(r.status_code))
            raise AuthException

    def _get_token(self):
        path = 'authtoken/Token.php'
        data = {
            "grant_type": "authorization_code",
            "code": self.code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": "https://google.com"
        }
        headers = {
            'Ocp-Apim-Subscription-Key': self.primary_key
        }
        r = requests.post(urljoin(self.base_url, path), data=data, headers=headers)
        self.auth_time = datetime.datetime.utcnow()
        self.token = Token(
            r.json()['access_token'],
            r.json()['refresh_token'],
            life=r.json()['expires_in'],
            received_at=datetime.datetime.utcnow()
        )

    def oauth(self):
        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username":self.username,
            "password":self.password,
            "er_aid":self.er_aid,
            "er_uid":self.er_uid,
            "scope":"https://login.emergencyreporting.com/secure/full_access",
            "response_type":"token"
        }  
        headers = {
            'Ocp-Apim-Subscription-Key': self.primary_key,
        }              
        r = requests.post(AUTH_URL, data=data, headers=headers)
        print(r.content)
        self.auth_time = datetime.datetime.utcnow()
        self.token = Token(
            r.json()['access_token'],
            # r.json()['refresh_token'],
            life=r.json()['expires_in'],
            received_at=datetime.datetime.utcnow()
        )

    def get_token(self):
        # self._get_auth_code()
        # self._get_token()
        self.oauth()

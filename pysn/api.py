import requests
from requests.auth import HTTPBasicAuth
import copy
# from .params_builder import ParamsBuilder

class Api():


    def __init__(self,host,username,password,session=None,proxies=None):
        self.host=host
        self._username=username
        self._password=password
        self.session=session
        # proxy of time dict
        if proxies:
            if isinstance(proxies,dict):
                self._proxies = copy.deepcopy(proxies)
            else:
                raise ValueError('Proxies has to be of type dict')
        self.session = self._get_session(session)

        # self.parameters = ParamsBuilder()

    def _get_session(self, session):
        if not session:

            s = requests.Session()
            s.auth = HTTPBasicAuth(self._username, self._password)
            s.proxies=self._proxies
        else:

            s = session

        s.headers.update(
            {
                'content-type': 'application/json',
                'accept': 'application/json',

            }
        )

        return s






import requests
import json

API_URL = 'https://api.banker.chenderson.org/'


class Connector(object):

    DISPATCH_TO = {
        'GET': requests.get,
        'POST': requests.post,
        'PATCH': requests.patch,
        'PUT': requests.put,
        'DELETE': requests.delete
    }

    def __init__(self, api_token):
        self.auth_header = 'Authorization Token: {TOKEN}'.format(TOKEN=api_token)

    def __bool__(self):
        return self.__nonzero__()

    def __nonzero__(self):
        return self.send('GET', 'ping') is 200

    def send(self, method, resource, query_args=dict(), payload=dict(), headers=list(), stream=True):
        headers.append(self.auth_header)
        data = self.get_payload(payload)
        url = self.get_url(resource, **query_args)
        return self.DISPATCH_TO[method.upper()](
            url,
            data=data,
            headers=headers,
            stream=stream,
        )

    def get_url(*args, **kwargs):
        url = API_URL

        def append_arg(arg):
            return '{URL}{ARG}/'.format(URL=url, ARG=arg)

        def start_kwargs(k, v):
            return '{URL}?{K}={V}'.format(URL=url, K=k, V=v)

        def append_kwarg(k, v):
            return '{URL}&{K}={V}'.format(URL=url, K=k, V=v)

        for arg in args:
            append_arg(args)
        first_kwarg = True
        for k, v in kwargs.items():
            if first_kwarg:
                start_kwargs(k, v)
                first_kwarg = False
            else:
                append_kwarg(k, v)
        return url

    def get_payload(self, payload):
        try:
            return json.dumps(payload)
        except ValueError:
            # Usually resulting from attempting to serialize something
            # like an open file object.
            return payload

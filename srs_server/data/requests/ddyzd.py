import requests

from flask import abort


class DDYZDService:
    url = 'https://developer-api.dsmkr.com/v1/info/basic/'

    @classmethod
    def get_inform(cls, token):
        print(token)
        res = requests.get(url=cls.url, headers={"access-token": f'Bearer {token}'})
        print(res.text)
        if res.status_code != 200: abort(401)
        return res.json()

import aiohttp


class AsyncHTTPClient:
    def __init__(self, *, session: aiohttp.ClientSession):
        self._session = session
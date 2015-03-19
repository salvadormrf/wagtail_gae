from django.core.cache.backends.memcached import BaseMemcachedCache
from google.appengine.api.memcache import Client


class GAEMemcachedCache(BaseMemcachedCache):
    "An implementation of a cache binding using python-memcached"
    def __init__(self, server, params):
        from google.appengine.api import memcache
        super(GAEMemcachedCache, self).__init__(
            server,
            params,
            library=memcache,
            value_not_found_exception=ValueError)

    @property
    def _cache(self):
        if getattr(self, '_client', None) is None:
            self._client = Client()
        return self._client

import redis
import json


class UniformCacheInterface:
    localreference = None

    def __init__(self):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def status(self):
        return self.localreference != None


class RedisCacheHandler(UniformCacheInterface):
    def __init__(self, host, port, db):
        r = redis.StrictRedis(host=host, port=port, db=db)
        try:
            r.set("ping", "pong")
            self.localreference = r
        except:
            self.localreference = None

    def get(self, key):
        value = self.localreference.get(key)
        if value:
            return json.loads(value)
        else:
            return None

    def set(self, key, value):
        self.localreference.set(key, json.dumps(value))


class LocalCacheHandler(UniformCacheInterface):
    def __init__(self):
        self.localreference = {}

    def get(self, key):
        value = self.localreference.get(key)
        if value:
            return value
        else:
            return None

    def set(self, key, value):
        self.localreference[key] = value


def init_cache_handlers(app):
    cache_redis = RedisCacheHandler('localhost', 6379, 0)
    if not cache_redis.status():
        app.logger.debug("Unable to connect to Redis. Using local caching")
        cache_redis = LocalCacheHandler()

    return cache_redis


if __name__ == '__main__':
    local = LocalCacheHandler()
    redis = RedisCacheHandler('localhost', 6379, 0)

    redis.set("my_key", "redis_my_value")
    print redis.get("my_key")

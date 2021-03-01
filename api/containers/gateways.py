from dependency_injector import containers, providers
from api.gateways import init_redis


class Gateways(containers.DeclarativeContainer):
    config = providers.Configuration()

    redis_pool = providers.Resource(init_redis, url=config.redis_url)

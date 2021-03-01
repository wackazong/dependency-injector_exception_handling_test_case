from dependency_injector import containers, providers
from . import Gateways
from api.repositories.listener_count_repository import ListenerCountRepository


class Repositories(containers.DeclarativeContainer):
    config = providers.Configuration()
    gateways = providers.Container(Gateways, config=config)

    listener_count = providers.Singleton(
        ListenerCountRepository,
        connection=gateways.redis_pool,
    )

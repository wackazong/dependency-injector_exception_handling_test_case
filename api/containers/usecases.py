from dependency_injector import containers, providers
from . import Repositories

from api.services.listener_count import Add


class ListenerCount(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()

    add = providers.Factory(Add, repo=repositories.listener_count)


class UseCases(containers.DeclarativeContainer):

    config = providers.Configuration()
    repositories = providers.Container(Repositories, config=config)
    listener_count = providers.Container(ListenerCount, repositories=repositories)

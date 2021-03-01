from dependency_injector import containers, providers
from . import Core, UseCases


class Application(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    core = providers.Container(Core)
    usecases = providers.Container(UseCases, config=config)

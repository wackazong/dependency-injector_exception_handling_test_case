class Add:
    def __init__(self, repo) -> None:
        self._repo = repo

    async def execute(self):
        await self._repo.get_listener_count()

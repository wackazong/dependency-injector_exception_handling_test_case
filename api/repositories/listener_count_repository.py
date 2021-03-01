from aioredis import Redis

LISTENER_COUNT_KEY = "ListenerCount"
CHECK_URL = "http://$ICECAST_HOST:$ICECAST_PORT/admin/listclients?mount=/$ICECAST_MOUNT"
LISTENERS_XPATH = './source[@mount="/radio"]/Listeners'


class ListenerCountRepository():
    def __init__(
        self,
        connection: Redis,
    ):
        self._connection = connection

    async def get_listener_count(self) :
        pass
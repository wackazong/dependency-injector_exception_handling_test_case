from typing import AsyncIterator
from aioredis import create_redis_pool, Redis


async def init_redis(url: str) -> AsyncIterator[Redis]:
    raise Exception
    pool = await create_redis_pool(url)
    yield pool
    pool.close()
    await pool.wait_closed()

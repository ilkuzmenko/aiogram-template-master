import asyncio
import asyncpg
import logging

from config import HOST, PG_PASS, PG_USER

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_pool():
    return await asyncpg.create_pool(user=PG_USER, password=PG_PASS, host=HOST)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

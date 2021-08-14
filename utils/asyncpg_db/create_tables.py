import asyncio
import os
import sys
import asyncpg
import logging

from config import PG_USER, PG_PASS, HOST

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_user_db():
    create_db_command = open(os.path.join(sys.path[0], "utils/asyncpg_db/user_db.sql"), "r").read()

    logging.info("Connecting to user table...")
    conn: asyncpg.Connection = await asyncpg.connect(user=PG_USER, password=PG_PASS, host=HOST)

    try:
        await conn.execute(create_db_command)
    except asyncpg.exceptions.DuplicateTableError:
        pass
    await conn.close()
    logging.info("Table USERS created")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_user_db())

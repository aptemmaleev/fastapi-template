import asyncio 

from app.api.server import start_api
from app.logger import setup
from app.settings import SETTINGS


async def main():
    # Setup logger
    setup()
    # Start server
    start_api()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.create_task(main())
    loop.run_forever()
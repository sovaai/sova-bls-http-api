from aiohttp import web
import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from routes import routes
import config
from tortoise import Tortoise
import logging
from kernel.tools import get_extension_models


if config.NLAB_SOVA_DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    sentry_sdk.init(
        dsn=config.NLAB_SOVA_SENTRY_DSN,
        integrations=[AioHttpIntegration()],
        release=config.NLAB_SOVA_VERSION
    )


async def main_start():
    """
        1. запуск приложения
    :return:
    """
    await Tortoise.init(
        db_url=config.NLAB_SOVA_DB_DSN,
        modules={
            'models': await get_extension_models()
        }
    )
    # Generate the schema
    await Tortoise.generate_schemas()
    app = web.Application(middlewares=[])
    app.add_routes(routes)
    return app

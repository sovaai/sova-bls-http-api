from aiohttp import web
import nest_asyncio
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from tortoise.contrib.test import initializer, finalizer
from external_modules.context.models import (Infs, Chat)
from routes import routes
from kernel.tools import get_extension_models


class TestRequestEndpoint(AioHTTPTestCase):
    """

    """
    async def setUpAsync(self) -> None:
        # db_url=config.DB_TEST_URL,
        initializer(await get_extension_models(), loop=self.loop)

    async def tearDownAsync(self) -> None:
        finalizer()

    async def get_application(self):
        nest_asyncio.apply()
        app = web.Application()
        app.add_routes(routes)
        return app

    @unittest_run_loop
    async def test_request_point_cuid_not_exist(self):
        """
            Для не существующего чата
        :return:
        """
        resp = await self.client.post(
            '/api/Chat.request',
            json={
                "cuid": "5d446bf7-1b32-4d2a-ad1f-d746c609ecc9",
                "text": "\u041d\u0435\u0442",
                "context": {
                    "isDevice": False,
                    "sys.rid": "0f0fd80d-c017-4ea6-a738-595ad7420012"
                }
            }
        )
        self.assertEqual(resp.status, 400)

    @unittest_run_loop
    async def test_request_point_cuid_exist(self):
        """
            Для существующего чата.
        :return:
        """
        inf = Infs(inf_profile='test')
        await inf.save()
        chat = Chat(inf=inf)
        await chat.save()
        resp = await self.client.post(
            '/api/Chat.request',
            json={
                "cuid": chat.cuid_str,
                "text": "\u041d\u0435\u0442",
                "context": {
                    "isDevice": False,
                    "sys.rid": "0f0fd80d-c017-4ea6-a738-595ad7420012"
                }
            }
        )
        self.assertEqual(resp.status, 200)
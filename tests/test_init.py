from aiohttp import web
import nest_asyncio
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from tortoise.contrib.test import initializer, finalizer
from external_modules.context.models import (Infs, Chat)
from routes import routes
from uuid import uuid4
from kernel.tools import get_extension_models


class TestInitEndpoint(AioHTTPTestCase):
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
    async def test_init_withoid_ciud_uuid_not_exist(self):
        """
            Проверяем эндпоинт когда не передается cuid и нет передаваемого uuid
            в базе данных
        :return:
        """
        resp = await self.client.post(
            '/api/Chat.init',
            json={
                "uuid": "c8054942-933c-4cc7-9327-2e7774735971",
                "context": {}
            }
        )
        self.assertEqual(resp.status, 400)

    @unittest_run_loop
    async def test_init_withoid_ciud_with_exist_uuid(self):
        """
            Проверяем эндпоинт когда не передается cuid и в базе данных uuid есть
        :return:
        """
        inf = Infs(uuid=uuid4(), inf_profile='test')
        await inf.save()

        resp = await self.client.post(
            '/api/Chat.init',
            json={
                "uuid": inf.uuid_str,
                "context": {}
            }
        )
        self.assertEqual(resp.status, 200)

    @unittest_run_loop
    async def test_init_with_ciud_and_uuid(self):
        """
            Проверяем эндпоинт когда передается cuid и в базе данных uuid есть
        :return:
        """
        inf = Infs(uuid=uuid4(), inf_profile='test')
        await inf.save()
        cuid = uuid4().__str__()

        resp = await self.client.post(
            '/api/Chat.init',
            json={
                "cuid": cuid,
                "uuid": inf.uuid_str,
                "context": {}
            }
        )
        self.assertEqual(resp.status, 400)

    @unittest_run_loop
    async def test_init_with_ciud_and_uuid_exist(self):
        """
            Проверяем эндпоинт когда передается cuid и в базе данных uuid, cuid есть
        :return:
        """
        inf = Infs(uuid=uuid4(), inf_profile='test')
        await inf.save()

        chat = Chat(inf=inf)
        await chat.save()

        resp = await self.client.post(
            '/api/Chat.init',
            json={
                "cuid": chat.cuid.__str__(),
                "uuid": inf.uuid_str,
                "context": {}
            }
        )
        self.assertEqual(resp.status, 200)
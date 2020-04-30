from aiohttp import web
from kernel.router import MessageHandler
import logging


class ChatInit(web.View):
    """
        Инициализация чата
    """
    async def post(self) -> web.Response:
        data = await self.request.json()
        message =await self.upgrade_info(data)
        m_handler = MessageHandler(message)
        message = await m_handler.process()
        if message.get("error"):
            return web.json_response(data=message['error'], status=m_handler.status_code)

        message = await self.generate_clean_resoponse(message)
        logging.info(f"Response {message}")
        return web.json_response(data=message, status=m_handler.status_code)

    async def upgrade_info(self, message):
        message['type'] = 'init'
        message['technical_info'] = {}
        return message

    async def generate_clean_resoponse(self, message):
        logging.debug(f"generate_clean_resoponse {message}")
        message.pop('uuid')
        message.pop('context')
        message.pop('type')
        message['inf'] = {"name": "text"}
        message['text'] = {"delay": 0}
        message['events'] = {}
        message['referer'] = None
        message['token'] = ''
        message['root'] = ''
        message.pop('technical_info')
        return {'result': message, 'id': 0}

from aiohttp import web
from kernel.router import MessageHandler
import datetime


class ChatEvent(web.View):

    async def post(self) -> web.Response:
        data = await self.request.json()
        message = await self.upgrade_info(data)
        m_handler = MessageHandler(message)
        message = await m_handler.process()
        if message.get("error"):
            return web.json_response(data=message['error'], status=m_handler.status_code)
        message = await self.clean_response(message)
        return web.json_response(data=message, status=m_handler.status_code)

    async def upgrade_info(self, message):
        message['type'] = 'event'
        message['technical_info'] = {
            "req_ts": datetime.datetime.now(),
        }
        return message

    async def clean_response(self, message):
        message.pop('type')
        message.pop('db_context')
        message.pop('technical_info')
        message.pop('euid')
        return {
            "result": {
                "text": {
                    "value": message['response']['text'],
                },
                "cuid": message['cuid'],
                "context": message['context'],
                "id": ""
            },
            "id": "0"
        }

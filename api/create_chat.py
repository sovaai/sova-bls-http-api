from aiohttp import web
from external_modules.context.models import Chat, Infs
import logging


class CreateChatHelper(web.View):

    async def post(self):
        inf = Infs(inf_profile='test', uuid='e888d15d-9c2e-4d00-9b9c-b9afb64c4751')
        await inf.save()
        chat = Chat(inf=inf)
        await chat.save()

        logging.debug(f"{dir(chat)}")
        logging.debug(f"{chat.__dict__}")

        data = {
            "inf": inf.uuid_str,
            "cuid": chat.cuid_str
        }
        return web.json_response(data=data, status=200)
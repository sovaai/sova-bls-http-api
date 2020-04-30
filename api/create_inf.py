from aiohttp import web
from external_modules.context.models import Infs


class CreateInfHelper(web.View):

    async def post(self):
        data = await self.request.json()
        try:
            inf = await Infs().create(uuid=data['buid'], inf_profile=data['profile'])
            inf.uuid = inf.uuid_str
            return web.json_response(data=inf.__dict__, status=200)
        except Exception as err:
            return web.json_response(data=err.__dict__, status=200)

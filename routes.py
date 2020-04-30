from api import (
    ChatRequest, ChatInit, ChatEvent, CreateInfHelper, CreateChatHelper
)
from aiohttp import web


routes = [
    web.post('/api/Chat.init', ChatInit, name='chat_init'),
    web.post('/api/Chat.request', ChatRequest, name='chat_request'),
    web.post('/api/Chat.event', ChatEvent, name='chat_event'),
    #TODO Вспомогательные методы. Удалить после разработки сервиса
    web.post('/api/create_inf', CreateInfHelper, name='create_inf'),
    web.post('/api/create_chat', CreateChatHelper, name='create_chat'),
]


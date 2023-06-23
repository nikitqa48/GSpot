from core.websocket.router.routing import WebSocketRouter
from core.redis import redis_manager
from core.database import db
from pydantic.error_wrappers import ValidationError
from src.messages.models import Message
from core.websocket.response import Response
from src.base.viewsets import WebSocketView

messages = WebSocketRouter()


@messages.add_endpoint('message')
async def send_message(request):
    try:
        message = Message.parse_obj(request.body)
    except ValidationError as e:
        return Response(status=1, reason=e)
    if request.action == 'create':
        await db.insert_collection('messages', message)
        await redis_manager.redis.publish(request.body['reciever'], 'text')
        return Response(status=0, data=message)
    if request.action == 'update':
        return Response(status=0, data='data')


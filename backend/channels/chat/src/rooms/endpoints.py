from core.websocket.router.routing import WebSocketRouter
from core.database import db
from core.websocket.response import Response
from .models import Room
from pydantic.error_wrappers import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status, File, Request
from .middleware import room_permission
from src.middlewares import get_token



rooms = WebSocketRouter()
http_rooms = APIRouter()


@rooms.add_endpoint('room')
async def handle_room(request):
    try:
        room = Room.parse_obj(request.body)
    except ValidationError as e:
        print('error', e)
        return Response(status=1, reason=e)
    if request.action == 'create':
        document_id = await db.insert_collection(collection_name='room', model=room)
        room.index = str(document_id)
        return Response.parse_obj({'status': 0, 'data': room, 'reason': 0})


@http_rooms.get('/room/{room_id}/', dependencies=[Depends(get_token)])
def get_messages(room_id: str, xz: dict = Depends(room_permission)):
    print(room_id)
    return {'key': 'ok'}

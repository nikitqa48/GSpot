from fastapi import APIRouter
from core.websocket.endpoints import ws
from core.websocket.router.routing import WebSocketRouter
from src.messages.endpoints.websocket import messages
from src.rooms.endpoints import rooms, http_rooms

ws_router = WebSocketRouter()
ws_router.include_router(messages)
ws_router.include_router(rooms)

router = APIRouter()
router.include_router(ws, tags=('websocket',))
router.include_router(http_rooms, tags=('messages', ))

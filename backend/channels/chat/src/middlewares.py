from fastapi import (
    Query,
    WebSocketException,
    status,
    Depends
)
import aiohttp
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
users = [1, 2]


def get_token(token: str = Depends(oauth2_scheme)):
    return True

    # async with aiohttp.ClientSession() as session:
    #     async with session.post('http://users/token', json={'token': token}) as resp:
    #         if resp.status != 201:
    #             raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    # return token

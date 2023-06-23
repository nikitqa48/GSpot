from fastapi import  Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from core.database import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
users = [1, 2]


def room_permission(request: Request):
    def wrapper():
        print(request.state.test)
        # user = request.user
        # print(dir(request))
        # print(request.url.property)
        return 'ok'
    return wrapper
from datetime import datetime, timedelta
from fastapi import HTTPException
import jwt
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from app.config import settings


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        if username == settings.ADMIN_EMAIL and password == settings.ADMIN_PASS:
            payload_jwt: dict = {
                "sub": username,
                "exp": datetime.utcnow() + timedelta(days=1),
            }
            token = jwt.encode(
                payload_jwt, key=settings.SECRET_KEY_JWT, algorithm=settings.ALGORITM
            )
            request.session.update({"token": token})
        else:
            raise HTTPException(status_code=401, detail="Неправильный логин или пароль")
        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        try:
            bool_token_decode = jwt.decode(
                token, key=settings.SECRET_KEY_JWT, algorithms=settings.ALGORITM
            )
        except:  # noqa: E722
            bool_token_decode = False
        if not token or bool_token_decode is False:
            return False
        return True

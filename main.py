from pathlib import Path
import uvicorn
from fastapi import FastAPI, Depends, Form,Request
from fastapi_users import FastAPIUsers
from starlette.responses import RedirectResponse
from auth.database import User
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from pages.router import router as router_pages, templates

app=FastAPI(
    title='Users'
)
app.include_router(router_pages)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user=fastapi_users.current_user()
# @app.get("/registration")
# async def get_registration(request:Request):
#     return templates.TemplateResponse("registration.html",{"request": request})
# @app.post("/registration")
# async def register(email: str = Form(), password: str = Form()):
#     print('email:', email)
#     print('password:', password)
#     return {"message": "Registration successful"}


@app.get('/protected-route')
def protected_route(user: User = Depends(current_user)):
    return f'Hellow,{user.username}'


@app.get('/unprotected-route')
def unprotected_route():
    return f'Hellow'

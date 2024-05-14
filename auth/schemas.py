from fastapi_users import schemas
from typing_extensions import Optional


class UserRead(schemas.BaseUser[int]):
    id:int
    email:str
    username:str
    is_active:bool=True
    is_superuser:bool=False
    is_verified:bool=False

    class Config:
        orm_mode=True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    username: str
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = False
    is_superuser: Optional[bool] = False

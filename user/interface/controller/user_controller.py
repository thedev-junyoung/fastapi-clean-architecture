
from fastapi import APIRouter, BackgroundTasks, Depends
from pydantic.v1 import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel): # 파이단틱의 모델을 사용하여 유저 생성 요청을 받는다.
    name: str
    email: str
    password: str

@router.post("", status_code=201)
def create_user(user: CreateUserBody): #
    user_service = UserService()
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password,
    )

    return created_user



# @router.post("", status_code=201)
# def create_user(
#     user: CreateUserBody,
#     # background_tasks: BackgroundTasks,
#     user_service: UserService = Depends(Provide[Container.user_service]),
#     # user_service: UserService = Depends(Provide["user_service"]),
# ):
#     created_user = user_service.create_user(
#         # background_tasks=background_tasks,
#         name=user.name,
#         email=user.email,
#         password=user.password,
#     )
#
#     return created_user

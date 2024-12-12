
from fastapi import APIRouter, BackgroundTasks, Depends

router = APIRouter(prefix="/users")

@router.post("", status_code=201)
def create_user():
    return "create_user"



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

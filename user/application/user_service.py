from datetime import datetime
from fastapi import BackgroundTasks, HTTPException, status
from passlib import crypto
from ulid import ULID

from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository



class UserService:
    def __init__(
        self,
        user_repo: IUserRepository,
        ulid: ULID,
        cryp
    ):
        self.user_repo = user_repo
        self.ulid = ulid
        self.crypto = crypto

    def create_user(
        self,
        # background_tasks: BackgroundTasks,
        name: str,
        email: str,
        password: str,
    ):
        _user = None
        try:
            _user = self.user_repo.find_by_email(email)
        except HTTPException as e:
            if e.status_code != 422:
                raise e

        if _user:
            raise HTTPException(status_code=422)

        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=self.crypto.encrypt(password),
            created_at=now,
            updated_at=now,
        )
        self.user_repo.save(user)


        return user

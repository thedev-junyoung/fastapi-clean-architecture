from abc import ABCMeta, abstractmethod

from user.domain.user import User


# 파이썬에서 제공하는 객체지향 인터페이스로 선언하기 위해 ABCMeta를 상속받는다.
class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        raise NotImplementedError

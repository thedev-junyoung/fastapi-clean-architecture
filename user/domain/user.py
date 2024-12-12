from dataclasses import dataclass
from datetime import datetime


@dataclass # 도메인 객체를 다루기 쉽도록 하기 위해 파이썬에서 제공하는 data class 데코레이터를 사용
class User:
    id: str
    name: str
    email: str
    password: str
    #memo: str | None
    created_at: datetime
    updated_at: datetime
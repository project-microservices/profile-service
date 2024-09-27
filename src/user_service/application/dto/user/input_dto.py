from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserRequest:
    user_uuid: str


@dataclass(frozen=True)
class CreateUserRequest:
    user_fullname: str
    user_country: str
    user_city: str
    user_age: int
    user_phone: str
    user_password: str
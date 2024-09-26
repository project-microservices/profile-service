from dataclasses import dataclass

from src.profile.domain.user.entity import UserEntity


@dataclass(frozen=True)
class GetUserResponse:
    id: int
    user_fullname: str
    user_country: str
    user_city: str
    user_age: int
    user_phone: str
    user_password: str

    @staticmethod
    def from_user_entity(user: UserEntity) -> 'GetUserResponse':
        return GetUserResponse(
            id=user.id.object,
            user_fullname=user.user_fullname.object,
            user_country=user.user_country.object,
            user_city=user.user_city.object,
            user_age=user.user_age.object,
            user_phone=user.user_phone.object,
            user_password=user.user_password.object
        )
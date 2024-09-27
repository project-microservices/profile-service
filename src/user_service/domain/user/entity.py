from dataclasses import dataclass

from src.user_service.domain.common.entities import CommonEntity
from src.user_service.domain.user.value_objects import (
    UserAge, UserCity, UserCountry, UserName, UserPassword, UserPhone, UserUUID
)


@dataclass(frozen=True)
class UserEntity(CommonEntity[UserUUID]):
    id: UserUUID
    user_fullname: UserName
    user_country: UserCountry
    user_city: UserCity
    user_age: UserAge
    user_phone: UserPhone
    user_password: UserPassword

    @staticmethod
    def create(
        id: str, user_fullname: str, user_country: str,
        user_city: str, user_age: int, user_phone: str,
        user_password: str
    ) -> 'UserEntity':
        return UserEntity(
            id=UserUUID(object=id),
            user_fullname=UserName(object=user_fullname),
            user_country=UserCountry(object=user_country),
            user_city=UserCity(object=user_city),
            user_age=UserAge(object=user_age),
            user_phone=UserPhone(object=user_phone),
            user_password=UserPassword(object=user_password)
        )
    

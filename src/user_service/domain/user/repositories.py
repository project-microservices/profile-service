from typing import Self, Protocol

from src.user_service.domain.user.entity import UserEntity
from src.user_service.domain.user.value_objects import (
    UserAge, UserCity, UserCountry, UserName, UserPassword, UserPhone, UserUUID
)


class UserInterface(Protocol):
    async def create_user(
        self: Self, user_uuid: UserUUID, user_fullname: UserName, user_phone: UserPhone, 
        user_password: UserPassword, user_city: UserCity, user_age: UserAge, user_country: UserCountry
    ) -> UserEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    async def delete_user(self: Self, user_uuid: UserUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    async def edit_user(
        self: Self, user_uuid: UserUUID, user_fullname: UserName | None, user_phone: UserPhone | None, 
        user_password: UserPassword | None, user_city: UserCity | None, user_age: UserAge | None, 
        user_country: UserCountry | None
    ) -> UserEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    async def get_user(self: Self, user_uuid: UserUUID) -> UserEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
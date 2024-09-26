from typing import Self, Protocol

from src.profile.domain.user.entity import UserEntity


class UserInterface(Protocol):
    async def create_user(
        self: Self, user_uuid: str, user_fullname: str, user_phone: str, 
        user_password: str, user_city: str, user_age: str, user_country: str
    ) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    async def delete_user(self: Self, user_uuid: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    async def edit_user(
        self: Self, user_uuid: str, user_fullname: str | None, user_phone: str | None, 
        user_password: str | None, user_city: str | None, user_age: str | None, 
        user_country: str | None
    ) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    async def get_user(self: Self, user_uuid: str) -> UserEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
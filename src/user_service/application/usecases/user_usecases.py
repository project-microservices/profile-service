from typing import Self
from uuid import uuid4, UUID

from src.user_service.domain.user.entity import UserEntity
from src.user_service.domain.user.repositories import UserInterface
from src.user_service.domain.user.value_objects import ( 
    UserAge, UserCity, UserCountry, UserName, UserPassword, UserPhone, UserUUID
)
from src.user_service.application.interactors.interactor import Interactor
from src.user_service.application.dto.user.input_dto import GetUserRequest, CreateUserRequest
from src.user_service.application.dto.user.output_dto import GetUserResponse, CreateUserResponse


class GetUserUseCase(Interactor[GetUserRequest, GetUserResponse]):
    def __init__(self: Self, user_gateway: UserInterface) -> None:
        self.user_gateway: UserInterface = user_gateway

    async def __call__(self: Self, request: GetUserRequest) -> GetUserResponse:
        user: UserEntity = await self.user_gateway.get_user(
            user_uuid=UserUUID(object=request.user_uuid)
        )

        return GetUserResponse.from_user_entity(user=user)
    

class CreateUserUseCase(Interactor[CreateUserRequest, CreateUserResponse]):
    def __init__(self: Self, user_gateway: UserInterface) -> None:
        self.user_gateway: UserInterface = user_gateway

    async def __call__(self: Self, request: CreateUserRequest) -> CreateUserResponse:
        user: UserEntity = await self.user_gateway.create_user(
            user_uuid=UserUUID(object=str(uuid4())),
            name=UserName(object=request.user_name),
            age=UserAge(object=request.user_age),
            phone=UserPhone(object=request.user_phone),
            password=UserPassword(object=request.user_password),
            country=UserCountry(object=request.user_country),
            city=UserCity(object=request.user_city)
        )

        return CreateUserResponse.from_user_entity(user=user)

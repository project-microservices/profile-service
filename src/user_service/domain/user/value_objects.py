from typing import Self

from src.user_service.domain.common.value_objects import DomainValueObject
from src.user_service.domain.common.exceptions import ValidationError


class UserUUID(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User uuid is required'
            )
        if not isinstance(self.object, str):
            raise ValidationError(
                f'User uuid must be a string, not {type(self.object)}'
            )
        
class UserName(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User name is required'
            )
        if not isinstance(self.object, str):
            raise ValidationError(
                f'User name must be a string, not {type(self.object)}'
            )
        
class UserAge(DomainValueObject[int]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User age is required'
            )
        if not isinstance(self.object, int):
            raise ValidationError(
                f'User age must be an integer, not {type(self.object)}'
            )
        
class UserCity(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User city is required'
            )
        if not isinstance(self.object, str):
            raise ValidationError(
                f'User city must be a string, not {type(self.object)}'
            )
        
class UserCountry(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User country is required'
            )
        if not isinstance(self.object, str):
            raise ValidationError(
                f'User country must be a string, not {type(self.object)}'
            )
        
class UserPhone(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User email is required'
            )
        if not isinstance(self.object, str):
            raise ValidationError(
                f'User email must be a string, not {type(self.object)}'
            )
        
class UserPassword(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise ValidationError(
                'User password is required'
            )
        if not isinstance(self.object, str):
            raise ValidationError(
                f'User password must be a string, not {type(self.object)}'
            )
        


from dataclasses import dataclass

from src.user_service.domain.common.value_objects import DomainValueObject


@dataclass
class CommonEntity[EntityID: DomainValueObject]:
    id: EntityID
    
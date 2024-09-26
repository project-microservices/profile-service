from dataclasses import dataclass


@dataclass
class CommonEntity[EntityID]:
    id: EntityID
    
from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserRequest:
    user_id: str
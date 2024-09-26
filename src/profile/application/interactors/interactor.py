from typing import Self, Protocol


class Interactor[InputDTO, OutputDTO](Protocol):
    async def __call__(self: Self, request: InputDTO) -> OutputDTO:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
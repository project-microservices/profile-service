from typing import AsyncIterator
from contextlib import asynccontextmanager

from faststream.asgi import AsgiFastStream
from faststream.nats import NatsBroker, NatsRouter


@asynccontextmanager
async def lifepan() -> AsyncIterator[None]:
    yield 

def init_logger() -> None:
    ...

def init_broker() -> NatsBroker:
    broker: NatsBroker = ...
    return broker

def init_routers() -> None:
    ...

def app_factory() -> AsgiFastStream:
    app: AsgiFastStream = AsgiFastStream()
    return app
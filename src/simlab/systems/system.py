# src/simlab/systems/system.py

from abc import ABC, abstractmethod

from simlab.systems.event import Event
from simlab.context import TickContext

class System(ABC):
    def __init__(self) -> None:
        self.name = self.__class__.__name__

    @abstractmethod
    def emit(self, context: TickContext) -> list[Event]:
        pass
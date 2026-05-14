# src/simlab/systems/system.py

from abc import ABC, abstractmethod

from simlab.systems.event import Event
from simlab.context import TickContext
from simlab.state import WorldState

class System(ABC):
    def __init__(self) -> None:
        self.name = self.__class__.__name__

    @abstractmethod
    def emit(self, context: TickContext, state: WorldState) -> list[Event]:
        pass
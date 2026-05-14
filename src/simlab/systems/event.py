# src/simlab/systems/event.py

from datetime import date 

from simlab.ids import identifier_registry


class Event:
    def __init__(
        self,
        event_id: str,
        event_type: str,
        system_name: str,
        payload: dict,
        tick: int,
        date: date,

    ) -> None:
        self.event_id = event_id
        self.event_type = event_type
        self.system_name = system_name
        self.payload = payload
        self.tick = tick 
        self.date = date
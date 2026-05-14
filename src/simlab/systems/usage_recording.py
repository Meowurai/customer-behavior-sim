# src/simlab/system/usage_recording.py

from simlab.systems import System, Event
from simlab.context import TickContext
from simlab.entities import UsageRecord
from simlab.ids import identifier_registry

class UsageRecordSystem(System):
    def __init__(self) -> None:
        super().__init__()

        self.identifier = identifier_registry.register_identifier('usage')

    def emit(self, context: TickContext) -> list[Event]:

        usage_id = self.identifier.new_id()
        usage_record = UsageRecord(
            usage_id=usage_id, 
            usage=context.rng.random()
        )

        event = Event(
            event_id=identifier_registry.new_id('event'),
            event_type="UsageRecorded",
            system_name=self.name,
            payload={
                "usage_record": usage_record
            },
            tick=context.tick,
            date=context.date
        )

        return [event]

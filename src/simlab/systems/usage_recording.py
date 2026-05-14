# src/simlab/system/usage_recording.py

from simlab.systems import System, Event
from simlab.context import TickContext
from simlab.state import WorldState
from simlab.entities import UsageRecord
from simlab.ids import identifier_registry

class UsageRecordSystem(System):
    def __init__(self) -> None:
        super().__init__()

        self.identifier = identifier_registry.register_identifier('usage')

    def emit(self, context: TickContext, state: WorldState) -> list[Event]:
        events: list[Event] = []
        customers = state.entity_data.get('customers')
         
        if customers is not None:
            for customer in customers:
                usage_id = self.identifier.new_id()
                usage_record = UsageRecord(
                    usage_id=usage_id, 
                    customer_id=customer.customer_id,
                    date=context.date,
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

                events.append(event)



        return events
# src/simlab/systems/customer_population.py

from simlab.systems import System, Event
from simlab.entities import Customer
from simlab.context import TickContext
from simlab.ids import identifier_registry

class CustomerPopulationSystem(System):
    def __init__(self) -> None:
        super().__init__()

        self.identifier = identifier_registry.register_identifier('customer')

    def emit(self, context: TickContext) -> list[Event]:
        events: list[Event] = []
        if context.tick == 1:
            
            for _ in range (5):
                customer = Customer(self.identifier)
                event = Event(
                    event_id=identifier_registry.new_id('event'),
                    event_type='CustomerCreated',
                    system_name=self.name,
                    payload={"customer": customer},
                    tick=context.tick,
                    date=context.date
                )
                events.append(event)

        return events

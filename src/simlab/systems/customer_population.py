# src/simlab/systems/customer_population.py

from simlab.systems import System, Event
from simlab.entities import Customer
from simlab.context import TickContext
from simlab.state import WorldState
from simlab.ids import identifier_registry

class CustomerPopulationSystem(System):
    def __init__(self) -> None:
        super().__init__()

        self.identifier = identifier_registry.register_identifier('customer')

    def emit(self, context: TickContext, state: WorldState) -> list[Event]:
        events: list[Event] = []
        if context.tick == 1:
            
            for _ in range (5):
                customer_id = self.identifier.new_id()

                # For now just init as 0.5
                usage_score = context.rng.uniform(0.5, 0.9)
                satisfaction_score = 0.5

                customer = Customer(
                    customer_id,
                    usage_score,
                    satisfaction_score
                    )
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

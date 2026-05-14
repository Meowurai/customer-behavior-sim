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
                customer = self.create_customer(context)
                event = self.create_event(context, customer)
                events.append(event)

        return events
    
    def create_event(self, context: TickContext, customer: Customer) -> Event:
        return Event(
                    event_id=identifier_registry.new_id('event'),
                    event_type='CustomerCreated',
                    system_name=self.name,
                    payload={"customer": customer},
                    tick=context.tick,
                    date=context.date
                )
    
    def create_customer(self, context: TickContext) -> Customer:
        customer_id = self.identifier.new_id()

        product_fit = context.rng.uniform(0.2, 0.9)
        usage_score = 0.0           # No usage has occurred yet
        satisfaction_score = 0.5    # Neutral satisfaction

        customer = Customer(
            customer_id,
            product_fit,
            usage_score,
            satisfaction_score
        )

        return customer

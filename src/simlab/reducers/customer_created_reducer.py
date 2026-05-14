# src/simlab/reducers/customer_created_reducer.py

from simlab.systems import Event
from simlab.state import WorldState
from simlab.entities import Customer

def reduce_customer_created(event: Event, state: WorldState) -> None:
    if not event.event_type == 'CustomerCreated':
        raise ValueError(f"reduce_customer_created got wrong event_type input {event.event_type}")
    
    customer: Customer | None = event.payload.get('customer')
    if customer is not None:
        state.entity_data.setdefault('customers', []).append(customer)
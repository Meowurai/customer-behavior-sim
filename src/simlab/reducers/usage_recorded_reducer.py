# src/simlab/reducers/usage_recorded_reducer.py

from simlab.systems import Event
from simlab.state import WorldState
from simlab.entities import UsageRecord

from statistics import mean


def reduce_usage_recorded(event: Event, state: WorldState):
    if not event.event_type == 'UsageRecorded':
        raise ValueError(f"reduce_usage_recorded got wrong event_type input {event.event_type}")
    
    usage_record: UsageRecord | None = event.payload.get('usage_record')
    if usage_record is not None:
        usage_records = state.entity_data.setdefault('usage_records', [])
        usage_records.append(usage_record)

        # Update customer record - must have link between
        customer_records = [
            r for r in usage_records
            if r.customer_id == usage_record.customer_id
        ]

        customers = state.entity_data.get("customers", [])
        customer = next(
            (c for c in customers if c.customer_id == usage_record.customer_id),
            None
        )
        if customer is not None:
            customer.usage_score = mean(r.usage for r in customer_records)

from simlab.systems import Event
from simlab.state import WorldState
from simlab.entities import UsageRecord, Customer


SATISFACTION_ADJUSTMENT_RATE = 0.03


def clamp(value: float, minimum: float, maximum: float) -> float:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def reduce_usage_recorded(event: Event, state: WorldState) -> None:
    if event.event_type != "UsageRecorded":
        raise ValueError(
            f"reduce_usage_recorded got wrong event_type input {event.event_type}"
        )

    usage_record: UsageRecord | None = event.payload.get("usage_record")
    if usage_record is None:
        raise ValueError("UsageRecorded event is missing usage_record payload")

    usage_records: list[UsageRecord] = state.entity_data.setdefault("usage_records", [])
    usage_records.append(usage_record)

    customers: list[Customer] = state.entity_data.get("customers", [])

    customer = next(
        (
            customer for customer in customers
            if customer.customer_id == usage_record.customer_id
        ),
        None,
    )

    if customer is None:
        raise ValueError(
            f"No customer found for usage_record customer_id {usage_record.customer_id}"
        )

    customer.usage_score = usage_record.usage_score

    target_satisfaction = usage_record.usage_score

    satisfaction_delta = (
        target_satisfaction - customer.satisfaction_score
    ) * SATISFACTION_ADJUSTMENT_RATE

    customer.satisfaction_score = clamp(
        customer.satisfaction_score + satisfaction_delta,
        0.0,
        1.0,
    )
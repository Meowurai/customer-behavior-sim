from simlab.systems import System, Event
from simlab.context import TickContext
from simlab.state import WorldState
from simlab.entities import UsageRecord
from simlab.ids import identifier_registry

SATISFACTION_USAGE_WEIGHT = 0.3
USAGE_NOISE_MIN = -0.1
USAGE_NOISE_MAX = 0.1

def clamp(value: float, minimum: float, maximum: float) -> float:
    if value < minimum:
        return minimum
    
    if value > maximum:
        return maximum

    return value

class UsageRecordSystem(System):
    def __init__(self) -> None:
        super().__init__()

        self.identifier = identifier_registry.register_identifier("usage")

    def emit(self, context: TickContext, state: WorldState) -> list[Event]:
        events: list[Event] = []

        customers = state.entity_data.get("customers", [])
        for customer in customers:
            expected_usage = customer.product_fit
            satisfaction_effect = (
                customer.satisfaction_score - 0.5
            ) * SATISFACTION_USAGE_WEIGHT

            noise = context.rng.uniform(USAGE_NOISE_MIN, USAGE_NOISE_MAX)
            usage_score = clamp(
                expected_usage + satisfaction_effect + noise,
                0.0,
                1.0,
            )

            usage_record = UsageRecord(
                usage_id=self.identifier.new_id(),
                customer_id=customer.customer_id,
                date=context.date,
                usage_score=usage_score,
            )

            event = Event(
                event_id=identifier_registry.new_id("event"),
                event_type="UsageRecorded",
                system_name=self.name,
                payload={"usage_record": usage_record},
                tick=context.tick,
                date=context.date,
            )

            events.append(event)

        return events
# src/simlab/simulation.py

from datetime import date, timedelta
from random import Random

from simlab.clock import Clock
from simlab.ids import identifier_registry
from simlab.context import TickContext
from simlab.state import WorldState
from simlab.systems import System, Event
from simlab.reducers import reduce_event_stats


class Simulation:
    def __init__(
        self, 
        systems: list[System],
        start_date: date, 
        ticks: int = 10, 
        delta: timedelta = timedelta(days=1),
        seed: int = 42
        
    ) -> None:
        self.systems = systems
        self.start_date = start_date
        self.ticks = ticks
        self.delta = delta

        self.rng = Random(seed)
        self.world_state = WorldState()

        identifier_registry.register_identifier('event')

    def run(self) -> None:
        clock = Clock(
            start_date=self.start_date, 
            ticks=self.ticks,
            delta=self.delta
        )

        while clock.is_running():
            context = TickContext(
                tick=clock.current_tick(),
                date=clock.current_date(),
                rng=self.rng
            )

            # Collect events from systems
            events: list[Event] = []
            for system in self.systems:
                system_events = system.emit(context, self.world_state)
                events.extend(system_events)

            # Reduce events to state
            for event in events:
                # Global reducers
                reduce_event_stats(event, self.world_state)


            
            # Summarize tick
            print(f"\nTick {clock.current_tick()} | {clock.current_date()}\n")

            for event in events:
                print(event.event_type)
                if event.payload.get("customer"):
                    customer_id = event.payload["customer"].customer_id
                    usage_score = event.payload["customer"].usage_score
                    satisfaction_score = event.payload["customer"].satisfaction_score

                    print(f"\n{' ' * 2} Customer: {customer_id}")
                    print(f"{' ' * 2} Usage Score: {usage_score}")
                    print(f"{' ' * 2} Satisfaction Score: {satisfaction_score}\n")

                if event.payload.get("usage_record"):
                    daily_usage = event.payload["usage_record"].usage
                    print(f"\n{' ' * 2} Daily Usage: {daily_usage}\n")


            # Advance time
            clock.advance()

        # Summarize simulation report
        print("Summary:\n")
        print(f"\nTotal processed events: {self.world_state.count_total_processed_events}")
        for event_type, count in self.world_state.count_event_types_events.items():
            print(f"{event_type}: {count}")

        print("\nEntity records created:\n")
        for entity, records in self.world_state.entity_data.items():
            print(f"{entity}: {len(records)}")

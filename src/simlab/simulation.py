# src/simlab/simulation.py

from datetime import date, timedelta
from random import Random

from simlab.report import tick_report, simulation_summary, SectionConfig, ReportConfig
from simlab.clock import Clock
from simlab.ids import identifier_registry
from simlab.context import TickContext
from simlab.state import WorldState
from simlab.systems import System, Event
from simlab.reducers import (
                                reduce_event_stats, 
                                reduce_customer_created,
                                reduce_usage_recorded
                            )


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
               
                # event type reducers:
                match event.event_type:
                    case 'CustomerCreated':
                        reduce_customer_created(event, self.world_state)
                    case 'UsageRecorded':
                        reduce_usage_recorded(event, self.world_state)

                    case _: 
                        print(f"Found event type with no reducer: {event.event_type}")

            
            # Summarize tick
            config = ReportConfig(
                events=SectionConfig(max_depth=4, max_items=3),
                state=SectionConfig(max_depth=4, max_items=5),
            )

            tick_report(
                clock=clock,
                events=events,
                state=self.world_state,
                config=config
            )


            # Advance time
            clock.advance()

        # Summarize simulation report
        simulation_summary(self.world_state, SectionConfig(max_depth=2))

        print()


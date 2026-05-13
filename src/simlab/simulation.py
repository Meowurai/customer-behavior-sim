# src/simlab/simulation.py

from datetime import date, timedelta

from simlab.clock import Clock
from simlab.ids import identifier_registry
from simlab.context import TickContext
from simlab.systems import System, Event


class Simulation:
    def __init__(
        self, 
        systems: list[System],
        start_date: date, 
        ticks: int = 10, 
        delta: timedelta = timedelta(days=1),
        
    ) -> None:
        self.systems = systems
        self.start_date = start_date
        self.ticks = ticks
        self.delta = delta

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
                date=clock.current_date()
            )

            # Collect events from systems
            events: list[Event] = []
            for system in self.systems:
                system_events = system.emit(context)
                events.extend(system_events)
            
            
            print(f"Tick {clock.current_tick()} | {clock.current_date()}")
            for event in events:
                print(event.event_type)
                print(event.payload)

            clock.advance()
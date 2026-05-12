# src/simlab/simulation.py

from datetime import date, timedelta

from simlab import Clock


class Simulation:
    def __init__(
        self, 
        start_date: date, 
        ticks: int = 10, 
        delta: timedelta = timedelta(days=1)
    ) -> None:
        self.start_date = start_date
        self.ticks = ticks
        self.delta = delta


    def run(self) -> None:
        clock = Clock(
            start_date=self.start_date, 
            ticks=self.ticks,
            delta=self.delta
        )

        while clock.is_running():
            print(f"Tick {clock.current_tick()} | {clock.current_date()}")
            clock.advance()
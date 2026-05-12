# src/simlab/clock.py

from datetime import date, timedelta

class Clock:
    """
    Simulation clock that runs between the start date and max_ticks.
    Time advanced based on the delta.
    """
    def __init__(self, start_date: date, ticks: int, delta: timedelta) -> None:
        self.start_date = start_date
        self.ticks = ticks
        self.delta = delta
        
        self._current_tick = 1
        self._current_date = self.start_date
        self._is_running = True # Initialize the clock as running

    def current_tick(self) -> int:
        """Returns the current simulation tick."""
        return self._current_tick
    
    def current_date(self) -> date:
        """Returns the current simulation date."""
        return self._current_date

    def is_running(self) -> bool:
        """Returns whether the simulation clock is running."""
        return self._is_running

    def advance(self) -> bool:
        """Advance simulation time by one tick and the set delta."""
        if self._current_tick < self.ticks:
            self._current_tick += 1
            self._current_date += self.delta
            return True 
        else:
            self._is_running = False
            return False
        

if __name__ == "__main__":
    clock = Clock(
        start_date=date(2026, 1, 1),
        ticks = 5,
        delta=timedelta(days=1)
    )

    while clock.is_running():
        print(f"Tick {clock.current_tick()} | {clock.current_date()}")
        clock.advance()

# src/simlab/main.py

from datetime import date, timedelta

from simlab import Simulation

def main():
    simulation = Simulation(
        start_date=date(2026, 1, 1),
        ticks=10,
        delta=timedelta(days=1)
    )

    simulation.run()
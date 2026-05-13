# src/simlab/main.py

from datetime import date, timedelta

from simlab import Simulation
from simlab.systems import CustomerPopulationSystem

def main():

    customer_population = CustomerPopulationSystem()

    simulation = Simulation(
        systems=[customer_population],
        start_date=date(2026, 1, 1),
        ticks=10,
        delta=timedelta(days=1)
    )

    simulation.run()
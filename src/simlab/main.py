# src/simlab/main.py

from datetime import date, timedelta

from simlab import Simulation
from simlab.systems import CustomerPopulationSystem, UsageRecordSystem

def main():

    # Init systems
    customer_population = CustomerPopulationSystem()
    usage_recording = UsageRecordSystem()

    # Init simulation
    simulation = Simulation(
        systems=[customer_population, usage_recording],
        start_date=date(2026, 1, 1),
        ticks=3,
        delta=timedelta(days=1),
        seed=42
    )

    # Run the simulation
    simulation.run()
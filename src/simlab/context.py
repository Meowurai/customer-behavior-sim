# src/simlab/context.py

from datetime import date
from random import Random

class TickContext:
    def __init__(self, tick: int, date: date, rng: Random):
        self.tick = tick 
        self.date = date 
        self.rng = rng
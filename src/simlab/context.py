# src/simlab/context.py

from datetime import date

from simlab.ids import IdentifierRegistry

class TickContext:
    def __init__(self, tick: int, date: date):
        self.tick = tick 
        self.date = date 
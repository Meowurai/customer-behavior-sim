# src/simlab/entities/usage.py
from datetime import date


class UsageRecord:
    def __init__(self, usage_id: str, customer_id: str, date: date,  usage: float) -> None:
        self.usage_id = usage_id
        self.customer_id = customer_id
        self.date = date
        self.usage = usage

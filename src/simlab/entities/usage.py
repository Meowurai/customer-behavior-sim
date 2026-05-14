# src/simlab/entities/usage.py
from datetime import date


class UsageRecord:
    def __init__(self, usage_id: str, customer_id: str, date: date,  usage_score: float) -> None:
        self.usage_id = usage_id
        self.customer_id = customer_id
        self.date = date
        self.usage_score = usage_score

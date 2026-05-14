# src/simlab/entities/usage.py


class UsageRecord:
    def __init__(self, usage_id: str, usage: float) -> None:
        self.usage_id = usage_id
        self.usage = usage
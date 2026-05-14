# src/simlab/state.py


class WorldState:
    def __init__(self) -> None:
        self.count_total_processed_events = 0
        self.count_event_types_events: dict[str, int] = {}

        self.entity_data: dict[str, list] = {}
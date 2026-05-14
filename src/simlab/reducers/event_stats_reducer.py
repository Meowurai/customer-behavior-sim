# src/simlab/reducers/revent_stats_reducer.py

from simlab.systems import Event
from simlab.state import WorldState

def reduce_event_stats(event: Event, state: WorldState) -> None:
    state.count_total_processed_events += 1
    state.count_event_types_events[event.event_type] = (
        state.count_event_types_events.setdefault(event.event_type, 0) + 1
    )

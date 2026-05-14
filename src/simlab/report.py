# src/simlab/report.py

from datetime import date, datetime

from simlab.clock import Clock 
from simlab.systems import Event 
from simlab.state import WorldState


class SectionConfig:
    def __init__(
        self,
        enabled: bool = True,
        max_depth: int = 10,
        max_items: int | None = None,
        show_root_class_name: bool = False,
        blank_line_between_items: bool = False,
    ) -> None:
        self.enabled = enabled
        self.max_depth = max_depth
        self.max_items = max_items
        self.show_root_class_name = show_root_class_name
        self.blank_line_between_items = blank_line_between_items

class ReportConfig:
    def __init__(
        self,
        events: SectionConfig | None = None,
        state: SectionConfig | None = None
    ) -> None:
        self.events = events or SectionConfig(max_depth=4, max_items=5)
        self.state = state or SectionConfig(max_depth=3, max_items=10)


def _is_simple(value: object) -> bool:
    return value is None or isinstance(
        value,
        str | int | float | bool | date | datetime,
    )


def _print_structure(
    value: object,
    indent: int = 0,
    max_depth: int = 10,
    max_items: int | None = None,
    current_depth: int = 0,
    show_root_class_name: bool = True,
    blank_line_between_items: bool = False,
) -> None:
    space = " " * indent

    if current_depth >= max_depth:
        print(f"{space}...")
        return

    if isinstance(value, dict):
        for key, item in value.items():
            if _is_simple(item):
                print(f"{space}{key}: {item}")
            else:
                print(f"{space}{key}:")
                _print_structure(
                    item,
                    indent + 2,
                    max_depth,
                    max_items,
                    current_depth + 1,
                    show_root_class_name,
                    blank_line_between_items,
                )

    elif isinstance(value, list):
        items = value if max_items is None else value[:max_items]

        for index, item in enumerate(items, start=1):
            if index > 1 and blank_line_between_items:
                print()

            _print_structure(
                item,
                indent + 2,
                max_depth,
                max_items,
                current_depth + 1,
                show_root_class_name,
                blank_line_between_items,
            )

        if max_items is not None and len(value) > max_items:
            remaining = len(value) - max_items
            print(f"{space}... {remaining} more items")

    elif hasattr(value, "__dict__"):
        show_this_class_name = show_root_class_name and current_depth == 0

        if show_this_class_name:
            class_name = value.__class__.__name__
            print(f"{space}{class_name}:")
            attr_indent = indent + 2
        else:
            attr_indent = indent

        attr_space = " " * attr_indent

        for attr_name, attr_value in vars(value).items():
            if attr_name.startswith("_"):
                continue

            if _is_simple(attr_value):
                print(f"{attr_space}{attr_name}: {attr_value}")
            else:
                print(f"{attr_space}{attr_name}:")
                _print_structure(
                    attr_value,
                    attr_indent + 2,
                    max_depth,
                    max_items,
                    current_depth + 1,
                    show_root_class_name,
                    blank_line_between_items,
                )

    else:
        print(f"{space}{value}")    
        

def tick_report(
    clock: Clock,
    events: list[Event],
    state: WorldState,
    config: ReportConfig | None = None,
) -> None:
    config = config or ReportConfig()

    print(f"\n> Tick {clock.current_tick()} | {clock.current_date()}\n")

    if config.events.enabled:
        print("Events:")
        _print_structure(
            events,
            indent=2,
            max_depth=config.events.max_depth,
            max_items=config.events.max_items,
            show_root_class_name=False,
            blank_line_between_items=True,
        )
    if config.state.enabled:
        print("\nWorld State:")
        _print_structure(
            state,
            indent=2,
            max_depth=config.state.max_depth,
            max_items=config.state.max_items,
            show_root_class_name=False,
            blank_line_between_items=True,
        )

def simulation_summary(
    state: WorldState,
    config: SectionConfig | None = None,
) -> None:
    config = config or SectionConfig(max_depth=4, max_items=10)

    summary = {
        "total_processed_events": state.count_total_processed_events,
        "event_counts": state.count_event_types_events,
        "entity_records_created": {
            entity: len(records)
            for entity, records in state.entity_data.items()
        },
    }

    print("\n\nSummary:")
    _print_structure(
        summary,
        indent=2,
        max_depth=3,
        max_items=None,
        show_root_class_name=False,
        blank_line_between_items=False,
    )

    customers = state.entity_data.get("customers")
    if customers is not None:
        print("\nFinal Customer State:")
        _print_structure(
            customers,
            indent=2,
            max_depth=config.max_depth,
            max_items=config.max_items,
            show_root_class_name=False,
            blank_line_between_items=True,
        )
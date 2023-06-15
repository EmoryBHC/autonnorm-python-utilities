from typing import Optional, Any


class RedcapRecord:
    def __init__(self, record: str, field_name: str, value: Any, event_name: Optional[str] = None, repeat_instrument: Optional[str] = None, repeat_instance: Optional[str] = None) -> None:
        self.record = record
        self.field_name: str = field_name
        self.value: str = str(value)
        self.redcap_event_name: Optional[str] = event_name  # Must be unique-event-name not event-label
        self.redcap_repeat_instrument: Optional[str] = repeat_instrument
        self.redcap_repeat_instance: Optional[str] = repeat_instance

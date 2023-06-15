from urllib.parse import urlsplit, parse_qs
import logging
from typing import Optional


class RedcapDataEntryTrigger:
    def __init__(self, event: dict) -> None:
        self.logger = logging.getLogger()
        trigger_dict = self._decode_event(event)
        self.redcap_url: str = trigger_dict["redcap_url"]
        self.project_url: str = trigger_dict["project_url"]
        self.project_id: str = trigger_dict["project_id"]
        self.username: str = trigger_dict["username"]
        self.record: str = trigger_dict["record"]
        self.redcap_event_name: Optional[str] = trigger_dict.get("redcap_event_name")
        self.instrument: Optional[str] = trigger_dict["instrument"]
        self.redcap_repeat_instance: Optional[str] = trigger_dict.get("redcap_repeat_instance")
        self.redcap_repeat_instrument: Optional[str] = trigger_dict.get("redcap_repeat_instrument")
        self.complete_status: int = self._get_complete(trigger_dict)

    def _decode_event(self, event) -> dict:
        body = event['body']
        self.logger.info("Decoding: " + str(body))

        url = "http://fakerul/?" + body
        query = urlsplit(url).query
        params = parse_qs(query)
        params_dict = dict(params)
        flat_params_dict = {k: v[0] for k, v in params.items()}
        return flat_params_dict

    def _get_complete(self, trigger_dict):
        try:
            complete_key = [key for key, value in trigger_dict.items() if '_complete' in key][0]
            return int(trigger_dict[complete_key][0])
        except:
            raise Exception("Could not get _complete field")

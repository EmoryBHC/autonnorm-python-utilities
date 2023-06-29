import requests
import logging
from datetime import datetime
from typing import List, Optional
from .project import RedcapProject
from .record import RedcapRecord


class RedcapController:
    def __init__(self) -> None:
        self.logger = logging.getLogger()

    def export_records(self,
                       project: RedcapProject,
                       record_ids: Optional[List[str]] = None,
                       instrument_names: Optional[List[str]] = None,
                       redcap_event_names: Optional[List[str]] = None,
                       redcap_repeat_instances: Optional[List[str]] = None,
                       redcap_repeat_instruments: Optional[List[str]] = None,
                       start_datetime: Optional[datetime] = None,
                       end_datetime: Optional[datetime] = None) -> List[RedcapRecord]:
        data = {
            'token': project.api_token,
            'content': 'record',
            'format': 'json',
            'type': 'eav',
            'csvDelimiter': '',
            'rawOrLabel': 'raw',
            'rawOrLabelHeaders': 'raw',
            'exportCheckboxLabel': 'false',
            'exportSurveyFields': 'false',
            'exportDataAccessGroups': 'false',
            'returnFormat': 'json',
            'records': record_ids,
            'events': redcap_event_names,
            'forms': instrument_names,
            'dateRangeBegin': start_datetime,
            'dateRangeEnd': end_datetime
        }

        raw_records: List[dict] = requests.post(project.api_url, data=data).json()
        self.logger.info('...Redcap Record Export Successful')
        self.logger.info('...Filtering Unrelated repeating instances of triggering instrument')

        records: List[RedcapRecord] = []
        self.logger.info('...Filtering successful')

        for raw_record in raw_records:
            if raw_record.get('redcap_repeat_instance') is not None and redcap_repeat_instances is not None and raw_record.get('redcap_repeat_instance') not in redcap_repeat_instances:
                continue
            if raw_record.get('redcap_repeat_instrument') is not None and redcap_repeat_instruments is not None and raw_record.get('redcap_repeat_instrument') not in redcap_repeat_instruments:
                continue

            records.append(RedcapRecord(
                record=raw_record['record'],
                event_name=raw_record.get('redcap_event_name'),
                repeat_instrument=raw_record.get('redcap_repeat_instrument'),
                repeat_instance=raw_record.get('redcap_repeat_instance'),
                field_name=raw_record['field_name'],
                value=raw_record['value']
            ))
        return records

    def import_records(self, project: RedcapProject, records: List[RedcapRecord]) -> dict:
        try:
            redcap_data: List[dict] = []
            for record in records:
                redcap_data.append(vars(record))

            data = {
                'token': project.api_token,
                'content': 'record',
                'format': 'json',
                'type': 'eav',
                'overwriteBehavior': 'normal',
                'forceAutoNumber': 'false',
                'data': '',
                'returnContent': 'count',
                'returnFormat': 'json',
                'data': redcap_data
            }
            self.logger.info('...Redcap Record Import Successful')
            response = requests.post(project.api_url, data=data)
            return response.json()
        except Exception as e:
            self.logger.info('...Redcap Record Import Unsuccessful')
            raise e

    def export_event_instrument_mappings(self, project: RedcapProject):
        data = {
            'token': project.api_token,
            'content': 'formEventMapping',
            'format': 'json',
            'returnFormat': 'json'
        }
        self.logger.info('...Redcap Event-Instrument Mappings Export Successful')
        response = requests.post(project.api_url, data=data)
        return response.json()

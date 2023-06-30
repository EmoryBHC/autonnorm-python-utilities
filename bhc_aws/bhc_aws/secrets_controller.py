import boto3
import logging
import json
from typing import Any


class SecretsController:
    def __init__(self, region_name: str = 'us-east-1') -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.region_name = region_name

    def get_secret(self, secret_name: str, *nested_secret_keys) -> Any:
        try:
            session = boto3.session.Session()
            secrets_manager_client = session.client(
                service_name='secretsmanager',
                region_name=self.region_name
            )

            get_secret_value_response = secrets_manager_client.get_secret_value(SecretId=secret_name)
            secret = json.loads(get_secret_value_response['SecretString'])
        except Exception as error_exception:
            self.logger.error({'error': str(error_exception), 'message': 'Failed retrieving secret'})
            raise

        if len(nested_secret_keys) == 0:
            return secret
        else:
            try:
                return self._get_nested(secret, *nested_secret_keys)
            except Exception as error_exception:
                self.logger.error({'error': str(error_exception),
                                  'message': 'Failed finding value within nested secret'})
                raise

    def _get_nested(self, dictionary: dict, *keys: tuple):
        if keys:
            key = keys[0]
            if key:
                try:
                    value = dictionary[key]
                except:
                    raise
                return value if len(keys) == 1 else self._get_nested(value, *keys[1:])

import json
from typing import Optional
from bhc_aws import LambdaRequestContext


class LambdaInvocation:
    def __init__(self, event: dict, context: dict, api_version: str):
        self.request_context: LambdaRequestContext = LambdaRequestContext(event['requestContext'])
        self.body: Optional[dict] = self.get_request_body(event)
        self.path: str = event["path"]
        self.context: dict = context
        self.api_version: str = api_version

    def get_request_body(self, event: dict):
        request_body = event.get("body")

        if request_body:
            return json.loads(request_body)
        else:
            return None

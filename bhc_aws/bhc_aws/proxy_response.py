from typing import Optional
import json
import logging


class ProxyResponse():
    def __init__(self, content: dict, status_code: int, isBase64Encoded: bool = False, headers: Optional[dict] = None):
        self.isBase64Encoded = isBase64Encoded
        self.statusCode = status_code
        self.body = json.dumps(content)
        self.headers = headers

    def as_dict(self) -> dict:
        response = {
            "isBase64Encoded": self.isBase64Encoded,
            "statusCode": self.statusCode,
            "body": self.body
        }
        if self.headers:
            response["headers"] = self.headers
        return response

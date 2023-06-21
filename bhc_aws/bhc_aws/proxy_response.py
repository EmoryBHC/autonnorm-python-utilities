from typing import Optional
import json
import logging


class ProxyResponse():
    def __init__(self, content: dict, status_code: int, isBase64Encoded: bool = False, headers: Optional[dict] = None):
        self.isBase64Encoded = isBase64Encoded
        self.statusCode = status_code
        self.body = json.dumps(content)
        if headers:
            self.headers = headers

    def as_dict(self) -> dict:
        # This function can be avoided by just calling vars(ProxyResponse(content=XXXX, status_code=XXXX)) directly
        return vars(self)

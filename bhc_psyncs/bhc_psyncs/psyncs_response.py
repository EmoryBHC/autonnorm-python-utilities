class PsyncsResponse:
    def __init__(self, response: dict, status_code: int) -> None:
        self.status_code = status_code
        self.status = response['status']
        self.message = response['message']
        self.datetime = response['datetime']
        self.version = response['version']

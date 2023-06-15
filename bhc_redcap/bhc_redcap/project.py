class RedcapProject:
    def __init__(self, redcap_url: str, api_token: str, project_id: int):
        self.redcap_url = redcap_url
        self.project_id = project_id
        self.api_url: str = self.redcap_url + 'api/'
        self.api_token = api_token

import requests
import logging
import json
import os
from .demographics import Demographics
from .enums import DemographicCoding
from .score import Score
from .psyncs_response_norm import PsyncsResponseNorm


class PsyncsController:
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        pass

    def post_normed_scores(self, raw_score: Score, test_id: int, score_id: int, norm_id: int, demographics: Demographics) -> PsyncsResponseNorm:
        demographics.coding = DemographicCoding.PSYNCS
        endpoint = "/normalized-scores"
        body = {
            "test_id": test_id,
            "score_id": score_id,
            "norm_id": norm_id,
            "raw_score": raw_score.value,
            "demographics": demographics.get_dict()
        }
        url = os.environ['PSYNCS_API_URL']
        if url is None:
            raise Exception("Could not get PSYNCS_API_URL environment variable")
        try:
            response = requests.post(url+endpoint, json.dumps(body))
        except Exception as e:
            raise e

        if response.status_code == 200:
            self.logger.info('Psyncs Call: Successful')
            return PsyncsResponseNorm(response.json(), status_code=response.status_code)
        elif response.status_code == 400:
            self.logger.info('Psyncs Call: Unsuccessful with Client Error')
            return PsyncsResponseNorm(response.json(), status_code=response.status_code)
        elif response.status_code == 500:
            self.logger.info('Psyncs Call: Unsuccessful with Server Error')
            return PsyncsResponseNorm(response.json(), status_code=response.status_code)
        else:
            self.logger.info('Psyncs Call: Unsuccessful with unknown error')
            raise Exception("Psyncs API Status != 200,400, or 500")

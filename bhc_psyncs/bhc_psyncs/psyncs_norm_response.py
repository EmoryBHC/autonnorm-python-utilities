from .normalized_scores import NormalizedScores
from .demographics import Demographics
from .score import Score
from .enums import ScoreModifier, ScoreType


class PsyncsNormResponse:
    def __init__(self, response: dict) -> None:
        self.status = response['status']
        self.datetime = response['datetime']
        self.version = response['version']
        self.message = response['message']

        self.test = response['test']
        self.score = response['score']
        self.norm = response['norm']

        self.scores = self.parse_scores(response['scores'])
        self.demographics = self.parse_demographics(response['demographics'])

    def parse_scores(self, scores: dict) -> NormalizedScores:
        modifier = None
        if scores.get('score_modifier') is not None:
            modifier = ScoreModifier(scores['score_modifier'])
        normalized_scores_params = {
            "raw_score": Score(ScoreType.RAW_SCORE, scores['raw_score']),
            "z_score": Score(ScoreType.Z_SCORE, scores['z_score'], modifier),
            "t_score": Score(ScoreType.T_SCORE, scores['t_score'], modifier),
            "scaled_score": Score(ScoreType.SCALED_SCORE, scores['scaled_score'], modifier),
            "standard_score": Score(ScoreType.STANDARD_SCORE, scores['standard_score'], modifier),
            "percentile": Score(ScoreType.PERCENTILE, scores['percentile'], modifier),
        }
        return NormalizedScores(**normalized_scores_params)

    def parse_demographics(self, scores: dict) -> Demographics:
        demographics_params = {
        }
        return Demographics(**demographics_params)

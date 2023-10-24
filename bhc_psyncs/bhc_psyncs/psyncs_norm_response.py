from .normalized_scores import NormalizedScores
from .demographics import Demographics
from .score import Score
from .enums import ScoreModifier, ScoreType, DemographicCoding


class PsyncsNormResponse:
    def __init__(self, response: dict, status_code: int) -> None:
        self.status_code = status_code
        self.status = response['status']
        self.message = response['message']
        self.datetime = response['datetime']
        self.version = response['version']

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

    def parse_demographics(self, demographics: dict) -> Demographics:
        demographics_params = {
            "coding": DemographicCoding.PSYNCS,
            "age": demographics['age'],
            "sex": demographics['sex'],
            "education": demographics['education'],
            "handedness": demographics['handedness'],
            "race": demographics['race'],
            "diagnosis": demographics['diagnosis'],
        }
        return Demographics(**demographics_params)

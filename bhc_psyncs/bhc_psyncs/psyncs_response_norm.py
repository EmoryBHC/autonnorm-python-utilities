from .normalized_scores import NormalizedScores
from .demographics import Demographics
from .score import Score
from .enums import ScoreModifier, ScoreType, DemographicCoding
from typing import Optional
from .psyncs_response import PsyncsResponse


class PsyncsResponseNorm(PsyncsResponse):
    def __init__(self, response: dict, status_code: int) -> None:
        super().__init__(response=response, status_code=status_code)
        self.test: Optional[str] = response.get('test')
        self.score: Optional[str] = response.get('score')
        self.norm: Optional[str] = response.get('norm')
        self.scores: Optional[NormalizedScores] = self.parse_scores(response.get('scores'))
        self.demographics: Optional[Demographics] = self.parse_demographics(response.get('demographics'))

    def parse_scores(self, scores: Optional[dict]) -> Optional[NormalizedScores]:
        if scores is None:
            return None
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

    def parse_demographics(self, demographics: Optional[dict]) -> Optional[Demographics]:
        if demographics is None:
            return None
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

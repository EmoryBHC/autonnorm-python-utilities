from copy import deepcopy
from typing import Optional
from .enums import ScoreType, ScoreModifier
from .score import Score


class Score:
    def __init__(self, type: ScoreType, value: float, modifier: Optional[ScoreModifier] = None):
        self.value: float = value
        self.type: ScoreType = type
        self.modifier: Optional[ScoreModifier] = modifier

    def rounded(self, places: int) -> Score:
        score = deepcopy(self)
        score.value = round(score.value, places)
        return score

    def string(self, round_places: Optional[int] = None):
        value = self.rounded(round_places) if round_places is not None else self.value
        modifier = self.modifier.value if self.modifier is not None else ""
        return modifier + str(value)

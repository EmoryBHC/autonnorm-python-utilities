from copy import deepcopy
from typing import Optional
from .enums import ScoreType, ScoreModifier


class Score:
    def __init__(self, type: ScoreType, value: float, modifier: Optional[ScoreModifier] = None):
        self.value: float = value
        self.type: ScoreType = type
        self.modifier: Optional[ScoreModifier] = modifier

    def rounded(self, places: int) -> float:
        value = deepcopy(self.value)
        return round(value, places)

    def string(self, round_places: Optional[int] = None):
        value = self.rounded(round_places) if round_places is not None else self.value
        modifier = self.modifier.value if self.modifier is not None else ""
        return modifier + str(value)

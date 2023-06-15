from enum import Enum


class ScoreModifier(Enum):
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL = "<="


class ScoreType(Enum):
    RAW_SCORE = 'raw_score'
    Z_SCORE = 'z_score'
    T_SCORE = 't_score'
    SCALED_SCORE = 'scaled_score'
    STANDARD_SCORE = 'standard_score'
    PERCENTILE = 'percentile'


class Race(Enum):
    AMERICAN_INDIAN_OR_ALASKAN_NATIVE = 0
    ASIAN = 1
    BLACK_OR_AFRICAN_AMERICAN = 2
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = 3
    WHITE = 4


class Handedness(Enum):
    RIGHT = 0
    LEFT = 1
    AMBIDEXTOROUS = 2


# Sex at birth
class Sex(Enum):
    FEMALE = 0
    MALE = 1


class DemographicCoding(Enum):
    HARMONIZED_BATTERY = 1
    PSYNCS = 2
    CUSTOM = 3


class DemographicVariableType(Enum):
    AGE = 1
    SEX = 2
    HANDEDNESS = 3
    RACE = 4
    DIAGNOSIS = 5
    EDUCATION = 6

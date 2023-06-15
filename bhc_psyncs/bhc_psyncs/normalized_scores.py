from .score import Score


class NormalizedScores:
    def __init__(self, raw_score: Score, z_score: Score, t_score: Score, scaled_score: Score, standard_score: Score, percentile: Score):
        self.raw_score = raw_score
        self.z_score = z_score
        self.t_score = t_score
        self.scaled_score = scaled_score
        self.standard_score = standard_score
        self.percentile = percentile

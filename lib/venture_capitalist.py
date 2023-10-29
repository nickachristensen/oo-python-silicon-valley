from .funding_round import FundingRound

class VentureCapitalist:
    _all = []

    def __init__(self, name, total_worth):
        self._name = name
        self._total_worth = total_worth
        self._funding_rounds = []
        self.__class__._all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def total_worth(self):
        return self._total_worth

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls._all if vc.total_worth > 1000000000]
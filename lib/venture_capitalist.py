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

    def offer_contract(self, startup, investment_type, amount_invested):
        funding_round = FundingRound(startup, self, investment_type, amount_invested)
        self._funding_rounds.append(funding_round)
        return funding_round

    @property
    def funding_rounds(self):
        return self._funding_rounds

    def portfolio(self):
        return list(set(round_.startup for round_ in self._funding_rounds))

    def biggest_investment(self):
        return max(self._funding_rounds, key=lambda round_: round_.investment, default=None)

    def invested(self, domain):
        return sum(round_.investment for round_ in self._funding_rounds if round_.startup.domain == domain)
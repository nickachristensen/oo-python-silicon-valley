class FundingRound:
    _all = []

    def __init__(self, startup, venture_capitalist, type_of_funding, investment):
        self._startup = startup
        self._venture_capitalist = venture_capitalist
        self._type = type_of_funding
        self._investment = max(investment, 0.0)
        self.__class__._all.append(self)

        startup._funding_rounds.append(self)
        venture_capitalist._funding_rounds.append(self)

    @property
    def startup(self):
        return self._startup

    @property
    def venture_capitalist(self):
        return self._venture_capitalist

    @property
    def type(self):
        return self._type

    @property
    def investment(self):
        return self._investment

    @classmethod
    def all(cls):
        return cls._all
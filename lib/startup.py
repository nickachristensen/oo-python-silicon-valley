from .funding_round import FundingRound

class Startup:
    _all = []

    def __init__(self, name, founder, domain):
        self._name = name
        self._founder = founder
        self._domain = domain
        self._funding_rounds = []
        self.__class__._all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def founder(self):
        return self._founder

    @property
    def domain(self):
        return self._domain

    def pivot(self, domain, name):
        self._domain = domain
        self._name = name

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_founder(cls, founder_name):
        for startup in cls._all:
            if startup.founder == founder_name:
                return startup

    @classmethod
    def domains(cls):
        return [startup.domain for startup in cls._all]
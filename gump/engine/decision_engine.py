from abc import ABC,abstractmethod

class DecisionEngine(ABC):

    @abstractmethod
    def decide(self,state,question=None):
        pass

    
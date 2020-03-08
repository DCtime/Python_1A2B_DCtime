from abc import ABC, abstractmethod


class Entity(ABC):

    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def guess(self):
        pass
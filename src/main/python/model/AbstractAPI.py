from abc import ABC, abstractmethod


class ConverterService(ABC):

    @abstractmethod
    def change(self, ammount, curFrom, curTo):
        pass

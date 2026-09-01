from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class Normal(Desconto):
    def calcular(self, valor):
        return valor * 0.1

class Vip(Desconto):
    def calcular(self, valor):
        return valor * 0.2

class Premium(Desconto):
    def calcular(self, valor):
        return valor * 0.3

from random import Random
from typing import Protocol


class StepCalculator(Protocol):
    def next(self, current_step: int) -> int:
        return 0


class NegatedStepper:
    def __init__(self, stepper: StepCalculator):
        self.__stepper = stepper

    def next(self, current_step: int) -> int:
        # to future self:
        # considere negar o current_step
        # -next(-current_step)
        return -self.__stepper.next(-current_step)


class CaesarStepper:
    def __init__(self, step: int):
        self.__step = step

    def next(self, current_step: int) -> int:
        return self.__step


class SeededStepper:
    """
    Nunca usar em produção para algo importante
    como uma cifra um stepper aleatório!
    Este stepper é para fins educativos.
    """

    def __init__(self, seed: int):
        self.rand = Random(seed)

    def next(self, current_step: int) -> int:
        return self.rand.randint(1, 100)


class ReverseBits:
    def next(self, current_step: int) -> int:
        # int: 4 bytes -> 32 bits
        # 10010010 00011100 01001100 10001001
        # 11111111 00001100
        # 00110000 11111111
        # 00000000 00000010

        new_step = 0
        sweeper = 1

        while sweeper <= 0x80_00_00_00:
            new_step |= bool(sweeper & current_step)
            new_step <<= 1
            sweeper <<= 1

        return new_step


class XorHalfs:
    def next(self, current_step: int) -> int:
        pass


class ShiftBytes:
    def next(self, current_step: int) -> int:
        pass

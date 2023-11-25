from random import Random
from typing import Protocol


class StepCalculator(Protocol):
    def next(self, current_step: int) -> int:
        raise NotImplementedError


class NegatedStepper:
    def __init__(self, stepper: StepCalculator):
        self.__stepper = stepper

    def next(self, current_step: int) -> int:
        # to future self:
        # considere negar o current_step
        # -next(-current_step)
        next_step = self.__stepper.next(current_step)
        return -next_step


class CaesarStepper:
    def next(self, current_step: int) -> int:
        return current_step


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
            new_step <<= 1
            new_step |= bool(sweeper & current_step)
            sweeper <<= 1

        return new_step


class XorHalfs:
    def next(self, current_step: int) -> int:
        raise NotImplementedError


class ShiftBytes:
    # 0x89ABCDEF
    # 0xABCDEF89
    # 0xCDEF89AB

    def __init__(self, direction='<', bytes_to_shift=1):
        self.direction = direction
        self.bytes_to_shift = bytes_to_shift

    def next(self, current_step: int) -> int:
        match (self.direction, self.bytes_to_shift):
            case ('<', 1):
                stamp = 0xffffff
                bits_to_shift = 8

            case ('<', 2):
                stamp = 0xffff
                bits_to_shift = 16

            case ('<', 3):
                stamp = 0xff
                bits_to_shift = 24

            case ('>', 1):
                stamp = 0xffffff00
                bits_to_shift = 8

            case ('>', 2):
                stamp = 0xffff0000
                bits_to_shift = 16

            case ('>', 3):
                stamp = 0xff000000
                bits_to_shift = 32

            case _:
                raise TypeError()

        left = current_step >> (32 - bits_to_shift)
        right = (current_step & stamp) << bits_to_shift
        return left | right

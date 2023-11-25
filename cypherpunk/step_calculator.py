from enum import IntFlag
from random import Random
from typing import Protocol


class StepCalculator(Protocol):
    def next(self, current_step: int) -> int:
        raise NotImplementedError


class NegatedStepper:
    def __init__(self, stepper: StepCalculator):
        self.__stepper = stepper

    def next(self, current_step: int) -> int:
        next_step = self.__stepper.next(-current_step)
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



class ShiftBitsDirection(IntFlag):
    LEFT  = 0b10
    RIGHT = 0b01


class ShiftBits:
    # 0xDEADBEEF
    # < 1 | > 3
    # 0xADBEEFDE
    # < 2 | > 2
    # 0xBEEFDEAD
    # < 3 | > 1

    def __init__(self, num_bytes=4,
                 direction=ShiftBitsDirection.LEFT, bits_to_shift=8):
        self.num_bits = num_bytes * 8
        self.bits_to_shift = bits_to_shift

        # se o número de bits pra shiftar for maior
        # do que o número de bytes, deve dar erro
        # mesma coisa se for menor do que 0
        if not (0 < self.bits_to_shift < self.num_bits):
            raise ValueError("bits_to_shift precisa ser menor que o número "
                             "de bits. " f"{bits_to_shift=}, {num_bytes*8=}")

        if direction not in ('<', '>'):
            raise ValueError('direction está errada')

        # inverte bits_to_shift se
        # direction == '>'
        if direction == '>':
            self.bits_to_shift = self.num_bits - bits_to_shift

    def next(self, current_step: int) -> int:
        bits_to_shift = self.bits_to_shift

        # abaixo leva em consideração
        # direction == '<'
        left = current_step << bits_to_shift
        left &= 0xffffffff

        right = current_step >> (32 - bits_to_shift)

        return left | right

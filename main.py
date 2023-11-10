import string

from cypherpunk.cypherpunk import Cypherpunk
from cypherpunk import step_calculator as sc


def main():
    cypher = Cypherpunk('hisnaelod')
    magic_value = 13
    stepper = lambda: sc.ReverseBits()

    cyphered = cypher.forth(
        'hello', magic_value, stepper())
    print(cyphered)

    original = cypher.back(
        cyphered, magic_value, stepper())
    print(original)

    assert original == 'hello'


if __name__ == '__main__':
    main()

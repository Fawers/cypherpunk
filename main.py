import string

from cypherpunk.cypherpunk import Cypherpunk
from cypherpunk import step_calculator as sc


def main():
    cypher = Cypherpunk(string.ascii_lowercase + ' ')
    stepper = lambda: sc.SeededStepper(1992)
    # rotate13 rot13

    original = 'aaabbc'
    encrypted = cypher.forth(original, 13, stepper())
    decrypted = cypher.back(encrypted, 13, stepper())

    print(f"{original=}, {encrypted=}")
    print(f"{decrypted=}, {original == decrypted = }")

if __name__ == '__main__':
    main()

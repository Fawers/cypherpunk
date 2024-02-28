import string

from cypherpunk.cypherpunk import Cypherpunk
from cypherpunk import step_calculator as sc

# TODO fazer o fawcrypt, que vai cuidar de
#      cifrar e decifrar um arquivo.

# TODO pacote cypherpunk no pypi

def main():
    cypher = Cypherpunk(string.ascii_lowercase + ' ')
    stepper = lambda: sc.ShiftBits(num_bytes=4, bits_to_shift=4)
    # rotate13 rot13

    original = 'aaabbc'
    encrypted = cypher.forth(original, 13, stepper())
    decrypted = cypher.back(encrypted, 13, stepper())

    print(f"{original=!r}, {encrypted=!r}")
    assert decrypted == original, f"{decrypted!r} != {original!r}"

if __name__ == '__main__':
    main()

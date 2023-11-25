import unittest

from cypherpunk import step_calculator as sc


class TestCaesarStepper(unittest.TestCase):
    def test_caesar_stepper_always_returns_same_step(self):
        stepper = sc.CaesarStepper()

        for _ in range(1000):
            self.assertEqual(stepper.next(13), 13)

class TestReverseBits(unittest.TestCase):
    def test_bits_get_reversed(self):
        input_step = [0b11111111_00000000_00000000_00000000,
                      0b00110011_11001100_01010101_10101010]
        expected   = [0b00000000_00000000_00000000_11111111,
                      0b01010101_10101010_00110011_11001100]

        stepper = sc.ReverseBits()

        for (a, b) in zip(input_step, expected):
            with self.subTest(input_step=a, expected=b):
                output = stepper.next(a)
                self.assertEqual(output, second=b)

class TestShiftBytes(unittest.TestCase):
    def test_shift_deadbeef_to_adbeefde(self):
        input_step = 0xdeadbeef
        expected = 0xadbeefde
        output = sc.ShiftBytes().next(input_step)

        self.assertEqual(output, expected)

    def test_shift_deadbeef_to_beefdead(self):
        input_step = 0xdeadbeef
        expected = 0xbeefdead
        output = sc.ShiftBytes(bytes_to_shift=2).next(input_step)

        self.assertEqual(output, expected)

    def test_shift_deadbeef_to_efdeadbe(self):
        input_step = 0xdeadbeef
        expected = 0xefdeadbe
        output = sc.ShiftBytes(bytes_to_shift=3).next(input_step)

        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()

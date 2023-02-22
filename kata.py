import pytest


class FizzBuzz:

    @staticmethod
    def compute(inputNumber: int):
        if inputNumber == 0:
            return '0'

        if inputNumber % 3 == 0:
            return 'Fizz'

        return '0'


class TestKata:

    def test_0(self):
        assert FizzBuzz.compute(0) == '0'

    def test_fizz(self):
        assert FizzBuzz.compute(3) == 'Fizz'



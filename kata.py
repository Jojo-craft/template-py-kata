import pytest


class FizzBuzz:

    @staticmethod
    def compute(inputNumber: int):
        if inputNumber == 0:
            return '0'

        if inputNumber % 3 == 0:
            return 'Fizz'

        if inputNumber % 5 == 0:
            return 'buzz'

        return str(inputNumber)


class TestKata:

    @pytest.mark.parametrize("test_input,expected", [(0, '0'), (1, '1'), (2,'2')])
    def test_eval(self,test_input, expected):
        assert FizzBuzz.compute(test_input) == expected

    def test_0(self):

        assert FizzBuzz.compute(0) == '0'

    def test_fizz(self):
        assert FizzBuzz.compute(3) == 'Fizz'

    def test_fizz_1(self):
        assert FizzBuzz.compute(1) == '1'

    def test_buzz(self):
        assert FizzBuzz.compute(5) == 'buzz'



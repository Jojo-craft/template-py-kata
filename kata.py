import pytest

FIZZ = 'Fizz'
BUZZ = 'buzz'
FIZZ_BUZZ = 'Fizz-buzz'


class FizzBuzz:

    @staticmethod
    def compute(input_number: int) -> str:
        if input_number == 0:
            return '0'

        if input_number % 15 == 0:
            return FIZZ_BUZZ

        if input_number % 3 == 0:
            return FIZZ

        if input_number % 5 == 0:
            return BUZZ

        return str(input_number)


class TestKata:

    @pytest.mark.parametrize("test_input", [3, 6, 9])
    def test_fizz(self, test_input):
        assert FizzBuzz.compute(test_input) == 'Fizz'

    @pytest.mark.parametrize("test_input", [5, 10, 50])
    def test_buzz(self, test_input):
        assert FizzBuzz.compute(test_input) == 'buzz'

    @pytest.mark.parametrize("test_input", [15, 30, 45, 60])
    def test_fizz_buzz(self, test_input):
        assert FizzBuzz.compute(test_input) == 'Fizz-buzz'

    @pytest.mark.parametrize("test_input, expected", [(0, '0'), (1, '1'), (2, '2')])
    def test_other_values(self, test_input, expected):
        assert FizzBuzz.compute(test_input) == expected

import pytest

from .data import temperatures
from .task import get_temperature_closest_to_zero


def test_get_temperature_closest_to_zero():
    assert 0.5 == get_temperature_closest_to_zero(temperatures)
    assert get_temperature_closest_to_zero([]) == 0
    assert get_temperature_closest_to_zero([-1, 2, 4, 0.2, 5, 3, -2, -0.1]) == -0.1
    assert get_temperature_closest_to_zero([1, 2, 3, 4, 5, 0, 11]) == 0
    assert get_temperature_closest_to_zero([11, -11]) == 11
    assert get_temperature_closest_to_zero([120, -3, 55]) == -3
    assert get_temperature_closest_to_zero([1, -1, 0.1]) == 0.1
    assert get_temperature_closest_to_zero([3, -3]) == 3

from .setup_env import *
from models.features import get_sum


def test_get_sum():
    assert (all([
        get_sum([1, 2, 3]) == 6,
        get_sum((1, 2, 3)) == 6,
        get_sum({1, 2, 3}) == 6
    ]))

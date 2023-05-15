from django_node.web_app.models.features import get_sum

def test_get_sum():
    assert (all([
        get_sum([1, 2, 3]) == 6,
        get_sum((1, 2, 3)) == 6,
        # get_sum({1, 2, 4}) == 6,
        get_sum({1, 2, 3}) == 6
    ]))

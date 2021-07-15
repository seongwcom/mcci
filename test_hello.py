from hello import add, multiply


def test_add():
    assert 2 == add(1, 1)

def test_multiply():
    assert multiply(10, 100) == 1000
    assert multiply(50, 2) == 100
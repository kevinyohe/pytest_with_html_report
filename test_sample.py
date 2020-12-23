from pytest import fixture



def inc():
    return 5



def test_answer():
    print("teseting inc")
    assert inc() == 5


def test_re():
    assert 1 ==1
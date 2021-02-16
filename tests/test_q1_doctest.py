import doctest_q1


def test_peq_1():
    result = doctest_q1.main(3, 5, 10)
    assert result == 23


def test_ans():
    result = doctest_q1.main(3, 5, 1000)
    assert result == 233168
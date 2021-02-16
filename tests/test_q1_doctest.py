import doctest_q1

def setup(setrange):
    global g_numrange
    g_numrange = setrange


def setnums(versusnum):
    calnumset = {num for num in range(1, g_numrange) if num % versusnum == 0}
    return calnumset


def Andcollections(num1, num2):
    return sum(setnums(num1) | setnums(num2))


def cal(num1, num2, range):
    """
    >>> cal(3, 5, 10)
    23
    >>> doctest_q1.main(3, 5, 1000)
    233168
    """
    setup(range)
    return Andcollections(num1, num2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
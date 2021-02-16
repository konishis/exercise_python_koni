"""
3 または 5 の倍数である 10 未満のすべての自然な数値をリストすると、3、5、6、9 が得られます。これらの倍数の合計は 23 です。
1000 以下の 3 または 5 のすべての倍数の合計を検索します。
"""


def setup(setrange):
    global g_numrange
    g_numrange = setrange


def setnums(versusnum):
    calnumset = {num for num in range(1, g_numrange) if num % versusnum == 0}
    return calnumset


def Andcollections(num1, num2):
    return sum(setnums(num1) | setnums(num2))


def main(num1, num2, range):
    setup(range)
    return Andcollections(num1, num2)
    
# def get_description():
#     """プロと同じようにランダムな天気を返す"""
    # from random import choice
    # possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    # return choice(possibilities)

#安全に書くならば
# def get_description():
#     import random
#     """プロと同じようにランダムな天気を返す"""
#     possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
#     return random.choice(possibilities)

#ほかの関数でもインポートしたコードを使う場合
import random
def get_description():
    """プロと同じようにランダムな天気を返す"""
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)
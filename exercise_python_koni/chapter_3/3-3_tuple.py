#tuple　イミュータブル　定数リスト

# empty_tuple = ()
# print(empty_tuple)

# one_marx = 'mike',#要素の最後の「,」は省略可
# print(one_marx)

# # marx_tuple = 'mike','chico','john'
# # print(marx_tuple)

# marx_tuple = ('mike','chico','john')#「()」を使っても意味は同じ
# print(marx_tuple)

#タプルのアンパック
# a, b, c = marx_tuple#一度に代入できる
# print(a)
# print(b)
# print(c)

#タプルだと一時変数を使わずに一つの文で値を交換できる
# breakfast = '食パン'
# dinner = 'フルコース'
# breakfast, dinner = dinner, breakfast
# print(breakfast)
# print(dinner)

#tuple()
food = ['食パン','フルコース']
print(food)
tupled_food = tuple(food)
print(tupled_food)
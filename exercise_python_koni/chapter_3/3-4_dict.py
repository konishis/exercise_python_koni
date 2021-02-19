# dict 辞書　イミュータブル型の一意なキーを与える

# empty_dict
# empty_dict = {}
# print(empty_dict)

# {}
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool"
# }
# print(dict1)

# dict()
# lol = [['nissan','skyline'],['mitsubishi','evo']]
# dict_lol = dict(lol)
# print(dict_lol)

# #dict() list of tuple
# lot = [('nissan','skyline'),('mitsubishi','evo')]
# dict_lot = dict(lot)
# print(dict_lot)

# #dict() tuple of list
# tol = (['nissan','skyline'],['mitsubishi','evo'])
# dict_tol = dict(tol)
# print(dict_tol)

# #dict() list of s
# los = ['ab','cd']
# dict_los = dict(los)
# print(dict_los)

# #dict() tuple of s
# tos = ('ab','cd')
# dict_tos = dict(tos)
# print(dict_tos)

# [key]
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool"
# }
# print(dict1)
# dict1['human'] = 'God'
# print(dict1)

# update
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# print(dict1)
# other = {
#     "john" : "genius",
#     "human" : "monkey",  #同じキーがある場合上書きされる
# }

# dict1.update(other)
# print(dict1)

# del
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# print(dict1)
# other = {
#     "john" : "genius",
#     "human" : "monkey",  #同じキーがある場合上書きされる
# }
# dict1.update(other)
# print(dict1)
# del dict1['john']
# print(dict1)

# clear
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# print(dict1)
# dict1.clear()
# print(dict1)

# in キーの有無
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# print(dict1)
# human_dict = 'human' in dict1
# print(human_dict)
# ambrose_dict = 'ambrose' in dict1
# print(ambrose_dict)
# john_dict = 'john' in dict1
# print(john_dict)

# [key]による要素の取得#1
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# tmp = dict1['human']
# print(tmp)

# [key]による要素の取得#2
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# tmp = dict1.get('human')
# print(tmp)

# [key]による要素の取得#3
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# tmp = dict1.get('boy','No data')
# print(tmp)

# keys()によるすべてのキーの取得
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# tmp = dict1.keys()
# print(tmp)
# tmp2 = list(dict1.keys())
# print(tmp2)

# values()によるすべての値の取得
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# tmp = dict1.values()
# print(tmp)

# items()によるすべてのキー/値ペアの取得
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# tmp = dict1.items()
# print(tmp)

# = and copy()#1
# dict1 = {
#     "ichigo" : "red and sweet",
#     "human" : "ambrose",
#     "mike" : "human and cool",
# }
# dict2 = dict1
# dict1['human'] = 'trush'
# print(dict1)
# print(dict2)

# = and copy()#2
dict1 = {
    "ichigo": "red and sweet",
    "human": "ambrose",
    "mike": "human and cool",
}
dict2 = dict1.copy()
dict1["human"] = "trush"
print(dict1)
print(dict2)
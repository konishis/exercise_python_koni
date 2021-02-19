# ex
# disaster = True
# if disaster:
#     print("Woe!")
# else:
#     print("Whee!")

# ex2
# color = "yellow"
# if color == "red":
#     print("red")
# elif color == "blue":
#     print("blue")
# elif color == "green":
#     print("green")
# else:
#     print("No just color:",color)

# while
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# break
# while True:
#     stuff = input("String to capitalize[type q to quit]")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

# continue
# while True:
#     value = input("Integer, please [q to quit]")
#     if value == 'q':    #終了
#         break
#     number = int(value)
#     if number % 2 == 0: #偶数
#         continue
#     print(number, "squared is",number*number)

# else
# numbers = [1,3,4,5,6]
# position = 0
# while position < len (numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print('Found even number', number)
#         break
#     position += 1
# else: # breakが呼ばれていない
#     print('No even number found')

# for#1
# rabbits = ['usagi','oisi','kanoyama']
# cpy = []
# for rabbit in rabbits:
#     print(rabbit)

# for#2
# word = 'cat'
# for letter in word:
#     print(letter)

# for#3
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictkey in word_dict:   #または　for dictkey in word_dict.keys():
#     print(dictkey)

# for#4
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictvalue in word_dict.values():
#     print(dictvalue)

# for#5
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictitem in word_dict.items():
#     print(dictitem)

# for#6 個々への代入
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictkey, dictvalue in word_dict.items():
#     print('dictkey : ', dictkey,',' 'dictvalue : ', dictvalue)

# zip#1
# days = ['Monday','Tuesday','Wednesday']
# fruits = ['banana','orange']
# drinks = ['beer','coffee','tea','soda']
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, ': drink', drink ,"fruit", fruit)

# zip#2 list
# days = ('Monday','Tuesday','Wednesday')
# nums = ('one', 'two', 'three','four')
# days_list = list(zip(nums, days))
# print(days_list)

# zip#3 dict
# days = ('Monday','Tuesday','Wednesday')
# nums = ('one', 'two', 'three','four')
# days_dict = dict(zip(nums, days))
# print(days_dict)

# range#1
# for x in range(100,0,-1):
#     print(x)

# range#2
# tmp = list(range(0,100,1))
# print(tmp)

# range#3
# tmp = list(range(0,101,2))
# print(tmp)

# list内包表記#1
# num_list = list(range(1,6,1))
# print(num_list)

# list内包表記#2 https://hibiki-press.tech/python/list-comprehensions/588
# num_list = [number for number in range(1,6)]
# print(num_list)

# list内包表記#3
# num_list = [number-1 for number in range(1,6)]
# print(num_list)

# list内包表記#4
# num_list = [number for number in range(1,7) if number % 2 == 0]
# print(num_list)

# list内包表記#5
# lows = range(0,100)
# highs = range(50,100)
# num_list = [(low, high) for low in lows for high in highs]
# for num in num_list:
#     print(num)

# list内包表記#5
# lows = range(0,100)
# highs = range(50,100)
# num_list = [(low, high) for low in lows for high in highs]
# for low, high in num_list:
#     print(low, high)

# ジェネレータ内包表記
# num_thing = (num for num in range(1,6))
# print(num_thing)
# for num in num_thing
# print(num)

# function#1
# def DoNothing():
#     pass

# DoNothing()

# function#2
# def MakeASounds():
#     print("quack")

# MakeASounds()

# function#3
# def ReturnTrue():
#     return True

# def checkReturn_True():
#     if ReturnTrue():
#         printString("OK")
#     else:
#         printString("OMG")

# def printString(String):
#     print(String)

# checkReturn_True()

# function#4
# def echoAnything(Anything):
#     return Anything + ' ' + Anything

# print(echoAnything('hello'))

# 位置関数 位置を覚えていれば対応付けできる
# def menu(wine, entree, dessert):
#     return {'wine':wine, 'entree': entree, 'dessert': dessert}

# print(menu('chardonnay','chicken', 'cake'))

# キーワード引数
# def menu(wine, entree, dessert):
#     return {'wine':wine, 'entree': entree, 'dessert': dessert}

# print(menu(entree='beef',wine='bordeaux',dessert='bage1'))

# デフォルト引数値
# def menu(drink1, drink2, entree, dessert='suger'):
#     return {'drink1':drink1,'drink2':drink2, 'entree': entree, 'dessert': dessert}

# print(menu(drink2='beer', entree='chicken',drink1='beer'))

# 位置引数のタプル化#1
# def print_args(*args):
#     print('入力値：',args)

# print_args()

# 位置引数のタプル化#2
# def print_args(*args):
#     print('入力値：',args)

# print_args(3,2,1,'wait!','uh...')

# 位置引数のタプル化#2
# def print_args(includeNum1,includeNum2, *args):
#     print('必須入力値1：',includeNum1)
#     print('必須入力値2：',includeNum2)
#     print('入力値：',args)

# print_args(3,2,1,'wait!','uh...')

# キーワード引数の辞書化
# def printKeyWords(**KeyWords):
#     print('keyword include:', KeyWords)

# printKeyWords(drink='beer',dessert='cake',human='human')

# docstrung
# def echo(thing, check):
#     '''
#     これは説明
#     トリプルクォーテーションで囲うこと
#     で複数行をコメントアウトできる
#     '''
#     if check:
#         print(thing)
# help(echo)
# print(echo.__doc__)

# object function#1
# def runSomething(func):
#     func()
# def answer():
#     print(42)

# runSomething(answer)
# print(type(runSomething))

# object function#2
# def add_args(arg1, arg2):
#     print(arg1 + arg2)

# print(type(add_args))

# object function#3
# def add_args(arg1, arg2):
#     print(arg1 + arg2)

# def runFunc_Twoinclude(func, arg1, arg2):
#     func(arg1,arg2)
# runFunc_Twoinclude(add_args,2,100)

# object function#4
# def sum_args(*args):
#     return sum(args)
# def runFunc_anyinclude(func, *args):
#     return func(*args)

# print(runFunc_anyinclude(sum_args,1,2,3,4,5,6,7,8,9,10))

# ジェネレータ
# print(sum(range(1,100)))


# original ジェネレータ
# def my_range(first=0,last=10,step=1):
#     num = first
#     while num < last:
#         yield num
#         num += step

# ranger = my_range(1,15)
# for x in ranger:
#     print(x)
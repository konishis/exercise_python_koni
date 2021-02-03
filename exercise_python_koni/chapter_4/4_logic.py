#ex
# disaster = True
# if disaster:
#     print("Woe!")
# else:
#     print("Whee!")
    
#ex2
# color = "yellow"
# if color == "red":
#     print("red")
# elif color == "blue":
#     print("blue")
# elif color == "green":
#     print("green")
# else:
#     print("No just color:",color)

#while
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

#break
# while True:
#     stuff = input("String to capitalize[type q to quit]")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

#continue
# while True:
#     value = input("Integer, please [q to quit]")
#     if value == 'q':    #終了
#         break
#     number = int(value)
#     if number % 2 == 0: #偶数
#         continue
#     print(number, "squared is",number*number)
    
#else
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
        
#for#1
# rabbits = ['usagi','oisi','kanoyama']
# cpy = []
# for rabbit in rabbits:
#     print(rabbit)

#for#2
# word = 'cat'
# for letter in word:
#     print(letter)

#for#3
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictkey in word_dict:   #または　for dictkey in word_dict.keys():
#     print(dictkey)
    
#for#4
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictvalue in word_dict.values():   
#     print(dictvalue)
    
#for#5
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictitem in word_dict.items():   
#     print(dictitem)

#for#6 個々への代入
# word_dict = {'hello': 'hello is こんにちは',
#              'dinner': 'dinner is 晩御飯',
#              'mike': 'mike is マイケル'}
# for dictkey, dictvalue in word_dict.items():   
#     print('dictkey : ', dictkey,',' 'dictvalue : ', dictvalue)
    
#zip#1
# days = ['Monday','Tuesday','Wednesday']
# fruits = ['banana','orange']
# drinks = ['beer','coffee','tea','soda']
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, ': drink', drink ,"fruit", fruit)

#zip#2 list
# days = ('Monday','Tuesday','Wednesday')
# nums = ('one', 'two', 'three','four')
# days_list = list(zip(nums, days))
# print(days_list)

#zip#3 dict
# days = ('Monday','Tuesday','Wednesday')
# nums = ('one', 'two', 'three','four')
# days_dict = dict(zip(nums, days))
# print(days_dict)

#range
for x in range(0,3):
    print(x)

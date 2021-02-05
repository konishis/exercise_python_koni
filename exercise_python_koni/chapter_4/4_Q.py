#4-1
# guess_me = 7
# if guess_me < 7:
#     print('too low')
# elif guess_me < 7:
#     print('too high')
# else:
#     print('just right')

#4-2
# guess_me = 7
# start = 1
# while True:
#     if  start< guess_me:
#         print('too low')
#     elif start == guess_me:
#         print('found it!')
#     else:
#         print('oops')
#         break
#     start += 1

#4-3
# for num in [3,2,1,0]:
#     print(num)

#4-4
# num_list = [num for num in range(10) if (num % 2 == 0)]
# print(num_list)

#4-5
# squares = {num : num * num for num in range(10)}
# print(squares)

#4-6
# odd = {num for num in range(10) if num % 2 == 1}
# print(odd)

#4-7
# num_thing = (num for num in range(10))
# for num in num_thing:
#     print('Got ',num)
#-----------
# for thing in ('Got %s' % number for number in range(10)):
#     print(thing)
    
#4-8
# def good():
#     good_list = ['Harry','Ron','Hermione']
#     return good_list

# print(good())
#-----------
# def good():
#     return ['Harry','Ron','Hermione']
# print(good())

#4-9
# def get_odds():
#     for num in range(1,10,2):
#         yield num

# for count , num2 in enumerate(get_odds(),1):
#     print(count,' ',num2) 

#original#1
# def includeRangeReturnNumber(INnum):
#     for cntNum in range(INnum):
#         yield cntNum

# def oddnumber(INnum):
#     for enucnt , enunum in enumerate(includeRangeReturnNumber(INnum),1):
#         if enucnt % 2 == 1:
#             yield enucnt

# exNUM = 11
# print(list(oddnumber(exNUM)))

#4-12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A run turns into a monster', 'Ahaunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)


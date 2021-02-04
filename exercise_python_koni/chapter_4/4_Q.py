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
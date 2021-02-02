lst = ['dog1','cat1','mouse1','dog2','cat2','dog2']
# lst[::-1]
# lst.pop(1)

#append
# lst.append('dog1')

#extend
# lst2 = ['mike','john']
# lst.extend(lst2)

#extend2
# lst2 = ['mike','john']
# lst += lst2

#append2
# lst2 = ['mike','john']
# lst.append(lst2)

#insert
# lst.insert(2,'moke')

#del
# del lst[-4]

#remove
# lst.remove('dog1')

#pop
# lst.pop()
#index
# tmp = lst.index('mouse1')
# print(tmp)

#in
# tmp = 'dog1' in lst
# tmp2 = 'mike' in lst
# print(tmp)
# print(tmp2)
# tmp = 'dog2' in lst 
# print(tmp)

#count
# tmp = lst.count('dog2')
# print(tmp)

#join and split
# separator = '*'
# joined = separator.join(lst)
# print(joined)
# separated = joined.split(separator)
# print(separated)
# print(lst)

#sort
# sorted_lst = sorted(lst)
# lst_num = [2,1,5.5,10,1.3]
# # sorted_lst_num = sorted(lst_num)
# lst_num.sort(reverse=True)
# print(lst_num)

#len
# len_lst = len(lst)
# print(len_lst)

#= and copy#1
# a = [1,2,3]
# print(a)
# b = a
# print(b)
# a[0] = 'aとbは同じリストobjを参照している'
# print(a)
# print(b)

#= and copy#2
# a = [1,2,3]
# print(a)
# b = a
# print(b)
# b[0] = 'aとbは同じリストobjを参照している'
# print(a)
# print(b)

#= and copy#3
# a = [1,2,3]
# b = a.copy()
# c = list(a)
# d = a[:]
# print(a)
# print(b)
# print(c)
# print(d)
# a[1] = '他はaのコピーのため、aを変更しても反映されない'
# print(a)
# print(b)
# print(c)
# print(d)


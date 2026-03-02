friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends, type(friends))
print(friends_tuple, type(friends_tuple))
print(friends_set, type (friends_set))

print(friends_set.intersection(my_friends_set))

print(my_friends_set.difference(set(friends)))

msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']

#print(list(msg),type(list(msg)))
print(msg.split(), type (msg.split()))
print(csv.split(','), type (csv.split()))
#print(friends_list.index('Michael'))
print(' '.join(friends_list), type(f''.join(friends_list)))

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']

#str1 = csv.replace(';', ',')
#print(str1.replace(':', ','))
friends_list = csv.replace(';', ',').replace(':', ',').split(',')
print(friends_list, type (friends_list))
#print(csv, type(csv.replace(';', ',')))
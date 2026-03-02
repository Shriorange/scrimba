names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
'''Print invitation for each frine using for loop
names in 2 lists. You also need to add 2 extra names to the list using input box when you runt he code. 
printout one invitation to each friend per line
Names sould be properyly capitalized
Example of printout:
John Cleese! You are invited to the party on saturday
hint: you may need 2 for loops to solve this exercise'''

#names.extend(names1)
all_names = names + names1
for get_name in range(1,3):
    get_name = str(input (f'Enter the name you want to add {get_name}: '))
    all_names.append(get_name)


for i in all_names:
    print(f' {i.title()}, You are invited to the party on saturday.'  )

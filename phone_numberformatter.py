# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

#phone_input = " (123)4567890 "

phone_input = str(input("Enter phone number to format: "))
phone_input = phone_input.strip()
phone_input = phone_input.strip()
phone_characters=['-','(',')','.']
for char in phone_characters:
    phone_input = phone_input.replace(char,'')

# phone_input = phone_input.replace('-','')
# phone_input = phone_input.replace('(','')
# phone_input = phone_input.replace(')','')
# phone_input = phone_input.replace('.','')

if (len(phone_input) == 10):
    newFormattedPhone_lst = list()
    phoneNumber_lst=list()
    phoneNumber_lst.append(phone_input[0:3])
    phoneNumber_lst.append(phone_input[3:6])
    phoneNumber_lst.append(phone_input[6:11])
    #lst = phone_input.split()
    templatePhone_lst= ['(',')','-']
    for i in range(len(templatePhone_lst)):
        newFormattedPhone_lst.append(templatePhone_lst[i])
        newFormattedPhone_lst.append(phoneNumber_lst[i])

    # newFormattedPhone_lst.append(templatePhone_lst[0])
    # newFormattedPhone_lst.append(lst[0])
    # newFormattedPhone_lst.append(templatePhone_lst[1])
    # newFormattedPhone_lst.append(lst[1])
    # newFormattedPhone_lst.append(templatePhone_lst[2])
    # newFormattedPhone_lst.append(lst[2])
    print(f'Your formatted phone number is {"".join(newFormattedPhone_lst)}')
else:
    print("Please enter exactly 10 digits.")







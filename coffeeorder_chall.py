# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

total_price = 0
drink_count = 0
while(True):
    customer_name = input("Customer name: ")
    if (customer_name == 'done'):
        break
    drink_order = input("Enter drink order (latte, americano, espresso):")
    if (drink_order == 'latte'):
        total_price = total_price + 3.50
        drink_count = drink_count + 1 
    elif (drink_order == 'americano'):
        total_price = total_price + 3
        drink_count = drink_count + 1 
    elif (drink_order == 'espresso'):
        total_price = total_price + 2.50
        drink_count = drink_count + 1 
    else:
        print("That is not in the menu, please try again") 
print(f'Total number of drink is {drink_count} and total price is {total_price:.2f}')

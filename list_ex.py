sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
#sales = []


input_sale = input ("Enter another sale for week 2: ")
sales_w2.append(int(input_sale))

print(sales_w2)
total_sales = sales_w1 + sales_w2
# find best and worst day of sale
total_sales.sort()
min_sales = total_sales[0]
max_sales = total_sales[-1]

profit_per_sale = 1.5

print(f'Best day of sales was {max_sales} and it sold for {max_sales*1.5}')
print(f'Worst day of sales was {min_sales} and it sold for {min_sales*1.5}')

""" #add another day to week2 list by capturing a number as input
sales_w2.append(int(input("Enter sales for day 7 of week 2: ")))

profit_per_sale = 1.5

#combine the two lists into one list
sales = sales_w1+sales_w2

#best day of sales
best_day = max(sales)
worst_day = min(sales)
print(f'Best day of sales is {best_day} and the sales was {best_day*profit_per_sale}')
print(f'Worst day of sales is {worst_day} and the sales was {worst_day*profit_per_sale}' """
      


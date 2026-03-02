def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    #return[tax, total_amount, amount]
    return f' {tax}, {total_amount}, {amount}'

x = value_added_tax(100)
print(x,  len(x), type(x))
#print(value_added_tax(100), type(value_added_tax(100)))

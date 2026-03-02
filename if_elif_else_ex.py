#print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def calculator_function(num1,num2,mode):
                        if(mode == '+'):
                            ans = num1 + num2
                        elif(mode == '-'):
                                ans = num1 - num2                            
                        elif(mode == '*'):
                                ans = num1 * num2
                        elif(mode == '/'):
                                ans = num1 / num2                                
                        return ans
def celcius_to_fahren(celcius_value):
        fahren = (celcius_value * 9/5) + 32
        return(fahren)

c = calculator_function(5,5,'/')
print(c, type(c))
print(celcius_to_fahren(30))
                        
    
    


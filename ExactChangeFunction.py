#the `exact_change()` function calculates the number of each coin type needed by performing integer division and modulus operations.
def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100

    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__':
    #Prompts the user to enter in the amount of change.
    input_val = int(input())
    #Calling the `exact_change()` to get the coin counts, and then prints the results.
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
#It checks the respective denominations, and if the count is greater than 1, it prints the denomination in plural form.
# Otherwise, it prints in singular form.     
    if num_dollars or num_quarters or num_dimes or num_nickels or num_pennies:
        if num_dollars:
            if num_dollars > 1:
                print(f"{num_dollars} dollars")
            else:
                print("1 dollar")
        
        if num_quarters:
            if num_quarters > 1:
                print(f"{num_quarters} quarters")
            else:
                print("1 quarter")
        
        if num_dimes:
            if num_dimes > 1:
                print(f"{num_dimes} dimes")
            else:
                print("1 dime")
        
        if num_nickels:
            if num_nickels > 1:
                print(f"{num_nickels} nickels")
            else:
                print("1 nickel")
        
        if num_pennies:
            if num_pennies > 1:
                print(f"{num_pennies} pennies")
            else:
                print("1 penny")
        
    else:
        print("no change")
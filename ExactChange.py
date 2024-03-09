#The code starts by taking an input change , which represents the total change amount.
change = int(input())
#goes through a series of calculations using integer division (// ) and modulus (% ) operations to determine the number of dollars, quarters, dimes, nickels, and pennies.
if change != 0:
    dollars = change // 100
    change %= 100
    quarters = change // 25
    change %= 25
    dimes = change // 10
    change %= 10
    nickels = change // 5
    change %= 5
    pennies = change
#It checks the respective denominations, and if the count is greater than 1, it prints the denomination in plural form.
# Otherwise, it prints in singular form.       
    if dollars:
        if dollars > 1:
            print(f"{dollars} Dollars")
        else:
            print("1 Dollar")
        
    if quarters:
        if quarters > 1:
            print(f"{quarters} Quarters")
        else:
            print("1 Quarter")
        
    if dimes:
        if dimes > 1:
            print(f"{dimes} Dimes")
        else:
            print("1 Dime")
        
    if nickels:
        if nickels > 1:
            print(f"{nickels} Nickels")
        else:
            print("1 Nickel")
        
    if pennies:
        if pennies > 1:
            print(f"{pennies} Pennies")
        else:
            print("1 Penny")
#If there is no change (i.e., change is 0), it prints "No change".
            
else:
    print("No change")
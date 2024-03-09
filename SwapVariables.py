#The swap_values function takes two integer arguments and returns them in swapped order. 
def swap_values(user_val1,user_val2):
    return user_val2, user_val1


if __name__ == '__main__': 
    #Prompts the user to enter in two integers.
    user_val1 = int(input())
    user_val2 = int(input())
    #calls the swap_values function, and prints the swapped values.
    swapped_val1, swapped_val2 = swap_values(user_val1, user_val2)
    #The print function outputs the swapped values separated by a space.
    print(swapped_val1, swapped_val2)
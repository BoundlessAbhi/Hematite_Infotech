print("Welcome to Password genrator")

lettersCapital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

letterSmall = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbolSome = ["~", "!", "@", "$", "%", "^", "&", "*", "-", "=", "+", "/"]

import random

def dynamicPassGen(x,y,z):
    '''Picking of x number of Capital letters from list'''
    PassCapi = random.sample(lettersCapital, k = x)
    print(PassCapi)
    print("\n")

    PassSmall = random.sample(letterSmall, k = y)
    '''Picking of x number of small letters from list'''
    print(PassSmall)
    print("\n")

    PassSymb = random.sample(symbolSome, k = z)
    '''Picking of x number of symbol from list'''
    print(PassSymb)
    print("\n")


    # adding all three randomly genrated list & and adding inpute numbers
    totall_length = x+y+z
    print(f"Totall length of your password is {totall_length} ")

    pass_aranged = PassCapi + PassSmall + PassSymb
    # print(pass_aranged)
    # print("\n")

    # Sufflling the list
    random.shuffle(pass_aranged)
    # print(pass_aranged)

    pass_finel = ""
    # converting list into string via loop
    for ren in pass_aranged:
        pass_finel = pass_finel + ren
    print(f"Here is your auto genratrd password : {pass_finel} \n")


def main():
    '''Getting three different input from user and
        sending them to dynamicPassGen Function'''
    user_Capi_length = int(input("How many Capital letter you want in your Password ?? : "))
    user_Small_length = int(input("How many Small letter you want in your Password ?? : "))
    user_Symb_length = int(input("How many Symbols you want in your Password ?? : "))
    dynamicPassGen(user_Capi_length,user_Small_length,user_Symb_length)
    
    again = int(input("If you want to genrate again enter 1 "))
    if again == 1:
        dynamicPassGen(user_Capi_length,user_Small_length,user_Symb_length)

    else:
        exit

if __name__ == "__main__":
    main()
print("Welcome to Password genrator")

# lettersCapital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# lettersSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# numbersNine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# symbolSome = ["!", "@", "#", "$", "%", "^", "&", "*", "~", "/" ]

allMIxUp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
            '~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '/'  ]

# allMIxUp = "abcdefghijklm"


import random


def my_random(x):
    print("hello")
    password = random.sample(allMIxUp, k = x)
    print(password)
    my_password = " "
    for i in password:
        my_password = my_password + i
    print(f"Here is your {x} length passwprd {my_password}")


def main():
    userPass_length = int(input("What should be password of length : "))
    my_random(userPass_length)

if __name__ == "__main__":
    main()
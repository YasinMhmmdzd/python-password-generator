import random
from colorama import Fore
print(Fore.BLUE + "welcome")
while True:
    password_range = int(input(Fore.LIGHTBLUE_EX + "Enter your password range (type 0 to close the programm) >>> "))
    allow_chars = ('aqzswxdecrfvgtbhynjumki,lo.p;[1234567890-=!@#$%^&*()_+/*-`~')
    if password_range >= 10 :
        for item in range(password_range):
            item = random.choice(allow_chars)
            print(Fore.GREEN + item , end='')
        print("")
    elif password_range == 0:
        break
    else:
        print(Fore.YELLOW + 'range should up to 10')

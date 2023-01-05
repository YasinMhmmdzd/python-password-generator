import random
from colorama import Fore
print(Fore.BLUE + "welcome")
password_range = int(input("Enter your password range"))
allow_chars = ('aqzswxdecrfvgtbhynjumki,lo.p;[1234567890-=!@#$%^&*()_+/*-`~')
if password_range >= 10 :
    for item in range(password_range):
        item = random.choice(allow_chars)
        print(Fore.GREEN + item , end='')
else:
    print('range should up to 10')

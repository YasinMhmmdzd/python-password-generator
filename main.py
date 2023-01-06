import random
from colorama import Fore
import pyperclip
print(Fore.BLUE + "welcome")
while True:
    chars = []
    password_range = int(input(Fore.LIGHTBLUE_EX + "Enter your password range " + Fore.LIGHTYELLOW_EX + "(type 0 to close the programm) >>> "))
    allow_chars = ('aqzswxdecrfvgtbhynjumki,lo.p;[1234567890-=!@#$%^&*()_+/*-`~')
    if password_range >= 10 :
        for item in range(password_range):
            item = random.choice(allow_chars)
            chars.append(item)
        new_password = ''.join(chars)
        print(Fore.GREEN + new_password)
        pyperclip.copy(new_password)
        print("password copid to clipboard !!!")
        print("")
    elif password_range == 0:
        break
    else:
        print(Fore.YELLOW + 'range should up to 10')

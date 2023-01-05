import random
print("welcome")
password_range = int(input("Enter your password range"))
allow_chars = ('aqzswxdecrfvgtbhynjumki,lo.p;[1234567890-=!@#$%^&*()_+/*-`~')
if int(password_range) > 10 :
    for item in range(password_range):
        item = random.choice(allow_chars)
        print(i , end='')
else:
    print('range should up to 10')

import random
def drivers(speed):
    if speed <= 70:
        print('you drive well',' the speed is:',speed)
        return
    a = speed - 70
    if a/5 >= 12:
        print('licence suspended',' the speed is:',speed)
    else:
        x = 0
        for i in range(0, a, 5):
            x = x + 1
        print('the number of demerit points is :', x,' the speed is:',speed)
def kill(cj):
    for i in range(cj):
        x = random.randint(40, 400)
        drivers(x)
kill(10)
kill(5)
from random import randint

def IsOddNumber(N):
    if N % 2 == 1:
        return True
    else:
        return False

for N in range(5):
    N = randint(1, 100)
    print("Число N ", N, " является нечетным: ", IsOddNumber(N))

 
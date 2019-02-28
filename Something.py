'''def red (R):
    if R < 0:
        return "ошибка"
    if R < 10:
        return R
    else:
        return red(R // 10) + (R % 10)
print(red(123))'''
def red (A):
    F = 2
    if A == 1:
        return False
    while F < A:
        if A % F == 0:
            return False
        F += 1
    return True

print(red(3**3**3**3+1))
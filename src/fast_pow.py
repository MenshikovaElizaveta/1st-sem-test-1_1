def fastPow(number, power):
    if power<0: 
        raise ValueError("Введена отрицательная степень")
    if power==0:
        return 1
    result = 1
    while power > 0:
        if (power%2)!=0:
            result *= number
        number *= number
        power = power // 2
    return result

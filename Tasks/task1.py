def IsEven(value):
    new_value = value // 2 * 2
    count = False
    if new_value == value:
        count = True
    return count


print(IsEven(int(input())))
# Вариант, описанный в примере имел плюс в простоте кода и его быстродействии.
# Минус моего варианта в использовании лишней переменной.


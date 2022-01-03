def check_division(num):
    if int(num) - num == 0:
        return True
    else:
        return False
print(check_division(4/3))
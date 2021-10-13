import random

def random_value(left_bound, right_bound):
    if left_bound > right_bound:
        raise ValueError("Unexpected values of boundaries")
    return random.randrange(left_bound, right_bound)

def sn_first_pattern(n):
    sum = 0;
    for i in range(1, n+1):
        sum += i*i*i
    return sum

def sn_secound_pattern(n):
    return (n*n*(n+1)*(n+1))/4


def compare_values(variable1, variable2):
    if variable1 == variable2:
        print("variables are equal")
    else:
        print("variables are not equal")

def zadanie9(n):
    sn1 = sn_first_pattern(n)
    sn2 = sn_secound_pattern(n)
    print("sn1: ",sn1)
    print("sn2: ",sn2)
    compare_values(sn1,sn2)


print("zadanie: 9")
HOW_MANY_TIMES = 3
for i in range(HOW_MANY_TIMES):
    value = random_value(1, 10)
    print("-------------------")
    print(value)
    zadanie9(value)
    print("-------------------")

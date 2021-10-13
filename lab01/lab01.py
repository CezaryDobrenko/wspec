import random

def get_n_th_value_in_arithmetic_sequence(a, r, n):
    if n < 0:
        raise ValueError("incorrect input data!")

    sum = a;
    for x in range(n-1):
        sum += r
    return sum

def zadanie_2(N, X, K):
    if K < 0 or N < 3:
        raise ValueError("incorrect input data!")

    for x in range(K):
        random_a = random.uniform(-X, X)
        random_r = random.uniform(-X, X)
        random_n = random.randint(3, N)
        n_th = get_n_th_value_in_arithmetic_sequence(random_a, random_r, random_n)
        print(n_th)

def zadanie_3(N, X, K):
    if K < 0:
        raise ValueError("K cannot be lesser than 0!")

    for x in range(K):
        random_a = random.uniform(-X, X)
        random_r = random.uniform(-X, X)
        random_n = random.randint(3, N)
        n_th_1 = round(get_n_th_value_in_arithmetic_sequence(random_a, random_r, random_n), 4)
        n_th_2 = round(random_a + (random_n - 1) * random_r, 4)
        print("-----------------")
        print(n_th_1)
        print(n_th_2)
        if n_th_1 == n_th_2:
            print("Correct comparasion")
        else:
            print("Incorrect comparasion")
        print("-----------------")



#Zadanie 1
n_th = get_n_th_value_in_arithmetic_sequence(1,2,5)
print(n_th)

#Zadanie 2
N = 20;
X = 5;
K = 10;
zadanie_2(N, X, K)

#Zadanie 3
N = 20;
X = 5;
K = 10;
zadanie_3(N, X, K)
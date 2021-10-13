# Recursion
# # złożoność czsowa: Powyższy algorytm wymaga n operacji przypisania oraz n-1 operacji odejnowania i n - 1 operacji dowania. Złożoność czasowa jest rzędu O(2n).
# # złożoność pamięciowa: Wymagana jest zmienna do przechowywania wartości sumowania. Złożoność pamięciowa jest rzędu O(1).


# Iteration
# # złożoność czsowa: Powyższy algorytm wymaga n operacji przypisania oraz n - 1 operacji dodawania. Złożoność czasowa jest rzędu O(n).
# # złożoność pamięciowa:Do przechowywania wartości obliczeń potrzebna jest jedna zmienna 𝑤𝑦𝑟𝑎𝑧_𝑐𝑖ą𝑔𝑢 niezależnie od n. Złożoność pamięciowa jest rzędu O(1).


# Pattern
# złożoność czsowa: Powyższy algorytm wymaga 1 operacja przypisania oraz 1 operacji dodawania, możenia i odejmowania. Złożoność czasowa jest rzędu O(1).
# złożoność pamięciowa:Do przechowywania wartości obliczeń potrzebna jest jedna zmienna 𝑤𝑦𝑟𝑎𝑧_𝑐𝑖ą𝑔𝑢 niezależnie od n. Złożoność pamięciowa jest rzędu O(1).


def an_pattern(a,r,n):
    return a + (n-1)*r

def an_iteration(a,r,n):
    an = a
    for i in range(n-1):
        an = an + r
    return an

def an_recursion(a,r,n):
    an = a
    if(n>1):
        an = an_recursion(a + r, r, n-1)
    return an

def sum_of_sequence(a1,an,n):
    return (a1 + an)*n/2

def sn_zadanie2_1(a,r,n):
    an = an_recursion(a,r,n)
    return sum_of_sequence(a,an,n)

def sn_zadanie2_2(a,r,n):
    an = an_iteration(a,r,n)
    return sum_of_sequence(a,an,n)


def sn_zadanie2_3(a,r,n):
    an = an_pattern(a,r,n)
    return sum_of_sequence(a,an,n)



def main():
    # Start variables
    n = 9
    a = 3
    r = 2

    s1 = sn_zadanie2_1(a, r, n)
    s2 = sn_zadanie2_2(a, r, n)
    s3 = sn_zadanie2_3(a, r, n)

    print("recursion: ", s1)
    print("iteration: ", s2)
    print("pattern: ", s3)

if __name__ == '__main__':
    main()
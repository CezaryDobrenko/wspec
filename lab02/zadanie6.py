def sum_of_sequence_reqursive(a,q,n):
    if q == 1:
        return a*n
    return (1-q**n)/(1-q)*a

def sum_of_sequence_iterative(a,q,n):
    result = a;
    for i in range(n):
        result = result * q
    return result

def sum_of_sequence_pattern(a,q,n):
    if q == 1:
        return a*n
    return (1-q**n)/(1-q)*a

def an_geometrical_recursive(a,q,n):
    an = a
    if (n > 1):
        an =an_geometrical_recursive(a * q, q, n - 1)
    return an

def an_geometrical_iterative(a,q,n):
    an = a
    for i in range(n-1):
        an = an*q
    return an

def an_geometrical_pattern(a,q,n):
    return a*q**(n-1)


def main():
    # Start variables
    n = 9
    a = 3
    q = 2

    print("an recursive: ", an_geometrical_recursive(a, q, n))
    print("an iterative: ", an_geometrical_iterative(a, q, n))
    print("an pattern: ", an_geometrical_pattern(a, q, n))

    print("sn rekurencynie: ", sum_of_sequence_reqursive(a, q, n))
    print("sn iteracyjnie: ", sum_of_sequence_iterative(a, q, n))
    print("sn pattern: ", sum_of_sequence_pattern(a, q, n))

if __name__ == '__main__':
    main()




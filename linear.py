import numpy as np


def first_test(A=40, E=100, R=15, L=20, nf=1, max_N=100):
    sol_N = 0
    for N in range(1, max_N + 1):
        if R + (nf + 1) * E + nf * A + L == N * 135:
            sol_N = N
            break
    return sol_N

    
def second_test(A=40, E=100, R=15, L=20, nf=1, max_N=100):
    
    A2_arr = np.arange(30, 50 + 5, 5)
    E1_arr = np.arange(230, 280 + 5, 5)
    
    sol_N = 0
    for N in range(1, max_N + 1):
        for A2 in A2_arr:
            for E1 in E1_arr:
                if R + nf * E + nf * A + E1 + L == N * 135 and E1 - E - A2 >= 100:
                    return N, A2, E1
    return 0, 0, 0


def third_test(A=40, E=100, R=15, L=20, nf=1, max_N=100):
    
    A2_arr = np.arange(30, 50 + 5, 5)
    A3_arr = np.arange(30, 120 + 5, 5)
    E1_arr = np.arange(230, 280 + 5, 5)
    E2_arr = np.arange(100, 235 + 5, 5)
    
    sol_N = 0
    for N in range(1, max_N + 1):
        for A2 in A2_arr:
            for A3 in A3_arr:
                for E1 in E1_arr:
                    for E2 in E2_arr:
                        if R + nf * E + nf * A + E1 + A3 + E2 + L == N * 135 and E1 - E - A2 >= 100:
                            return N, A2, A3, E1, E2
    return 0, 0, 0, 0, 0


A = 40
E = 100
R = 15
L = 15
nf = 16
max_N = 100


N = first_test(A=A, E=E, R=R, L=L, nf=nf, max_N=max_N)

if N > 0:
    print("For nf =", nf)
    print("Use 1st dummy PO, N =", N)

if N == 0:
    N, A2, E1 = second_test(A=A, E=E, R=R, L=L, nf=nf, max_N=max_N)
    if N > 0:
        print("For nf =", nf)
        print("Use 2nd dummy PO")
        print("N =", N)
        print("A2 =", A2)
        print("E1 =", E1)
    if N == 0:
        N, A2, A3, E1, E2 = third_test(A=A, E=E, R=R, L=L, nf=nf, max_N=max_N)
        print("For nf =", nf)
        print("Use 3rd dummy PO")
        print("N =", N)
        print("A2 =", A2)
        print("A3 =", A3)
        print("E1 =", E1)
        print("E2 =", E2)







import matplotlib.pyplot as plt
import numpy as np

def gp_general_term(a, d, n):
    if n>=0:
        return a+n*d
    else:
        return 0

def plot_gp_general_term(a, d, start, end):
    n_values = np.arange(start, end + 1, 1)
    ap_values = [gp_general_term(a, d, n) for n in n_values]

    plt.stem(n_values, ap_values, basefmt='b-', linefmt='d-', markerfmt='ro')
    plt.title('General Term of Arithematic Progression')
    plt.xlabel('n')
    plt.ylabel('Term Value')
    plt.grid(True)
    plt.show()

a = 120  
d=5
r = 2
start_n = -2
end_n = 15
plot_gp_general_term(a, d, start_n, end_n)

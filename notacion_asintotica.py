# ley de la multipicación
import time

# crecimiento cuadratico.

def f(n):
    cominezo = time.time()
    for i in range(n):
        for j in range(n):
            print(i,j)
    final = time.time()
    print(final - cominezo)


# Recursividad múltiple
def fibonachi(n):
    if n == 0 or n == 1:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)

def main():
    f(10)
    print(fibonachi(10))
    
if __name__ == '__main__':
    main()
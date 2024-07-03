# Función para calcular el n-ésimo número de Fibonacci utilizando memorización
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

# Función para imprimir la serie de Fibonacci hasta el número dado
def imprimir_fibonacci_hasta(numero):
    for i in range(numero):
        print(fibonacci(i), end=" ")
    print()

# Función para calcular la suma de los primeros n números de Fibonacci
def suma_fibonacci(n):
    total = 0
    for i in range(n):
        total += fibonacci(i)
    return total

# Función para calcular la razón dorada aproximada utilizando los números de Fibonacci
def razon_dorada(n):
    if n < 2:
        raise ValueError("n debe ser al menos 2 para calcular la razón dorada.")
    return fibonacci(n) / fibonacci(n-1)

# Ejemplo de uso:
limite = 10
print(f"Serie de Fibonacci hasta el número {limite}:")
imprimir_fibonacci_hasta(limite)

suma = suma_fibonacci(limite)
print(f"Suma de los primeros {limite} números de Fibonacci: {suma}")

n = 10
razon = razon_dorada(n)
print(f"Razón dorada aproximada usando Fibonacci({n}) y Fibonacci({n-1}): {razon}")

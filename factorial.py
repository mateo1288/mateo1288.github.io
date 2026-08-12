def fibonacci(n):
    print(f"Entrando a fibonacci({n})")  # Muestra el recorrido

    if n == 0:  # Caso base
        print(f"Retornando {n}")
        return 0
    elif n == 1:  # Caso base
        print(f"Retornando {n}")
        return 1
    else:
        resultado = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"Retornando {resultado} desde fibonacci({n})")
        return resultado

def mostrar(n):
    if n >= 0:
        mostrar(n - 1)
        print(f"\nResultado Fibonacci({n}) = {fibonacci(n)}")

mostrar(4)

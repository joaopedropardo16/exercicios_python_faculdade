n1 = float(input("Digite um número"))
n2 = float(input("Digite outro número"))
op = input("Informe uma operação ( +, -, *, / )")

if op == '+':
    print(f"Soma dos números: {n1 + n2}")
elif op == '-':
    print(f"Subitração dos números: {n1 - n2}")
elif op == '*':
    print(f"Multiplicação dos números: {n1 * n2}")
elif op == '/':
    print(f"Divisão dos números: {n1 / n2:.1f}")
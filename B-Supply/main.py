def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Program Deret Fibonacci")
    n = int(input("Masukkan jumlah elemen Fibonacci yang ingin dihitung: "))
    print(f"Deret Fibonacci hingga elemen ke-{n}:")
    for i in range(n):
        print(fibonacci(i), end=" ")

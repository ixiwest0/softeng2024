from hw02_even_odd import is_even

def even_sum(s, e):
    return sum([i for i in range(s, e+1) if is_even(i)])

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b(b > a): "))

    print(f"{a}부터 {b}까지의 짝수의 합은 {even_sum(a, b)}입니다.")

if __name__ == "__main__":
    main()
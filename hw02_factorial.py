def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def main():
    n = int(input("Enter num: "))
    print(f"{n}까지의 팩토리얼 수는 {fact(n)}입니다.")


if __name__ == "__main__":
    main()
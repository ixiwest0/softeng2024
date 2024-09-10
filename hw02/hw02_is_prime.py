def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter num: "))
    print(f"{n}은 소수가 {["아닙니다.", "맞습니다."][int(is_prime(n))]}")

if __name__ == "__main__":
    main()
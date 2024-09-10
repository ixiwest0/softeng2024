from hw02_is_prime import is_prime

def primenum(num):
    return [i for i in range(2, num + 1) if is_prime(i)]

def main():
    n = int(input("2이상의 정수를 입력해주세요.: "))
    print(f"{n}이하의 정수 중 소수는 {primenum(n)}입니다.")

if __name__ == "__main__":
    main()
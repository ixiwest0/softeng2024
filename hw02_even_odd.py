def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def main():
    even_odd = ["홀수", "짝수"]
    num = int(input("Enter num: "))
    print(f'{num}은 {even_odd[int(is_even(num))]}입니다.')
    

if __name__ == "__main__":
    main()
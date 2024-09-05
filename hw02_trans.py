def trans_temp(tp, temp):
    if tp == "f":
        return (temp * 1.8) + 32
    else:
        return (temp - 32) / 1.8
    
def main():
    tp = input("원하는 타입을 입력해주세요. 화씨로 변환하고 싶으면 f를, 섭씨로 변환하고 싶으면 c를 입력해주세요.: ")
    temp = int(input("온도를 입력해주세요.: "))

    if tp == "f":
        print(f"{temp}f => {trans_temp(tp, temp)}c")
    else:
        print(f"{temp}c => {trans_temp(tp, temp)}f")
        
if __name__ == "__main__":
    main()
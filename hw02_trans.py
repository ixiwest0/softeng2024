def trans_temp(tp, temp):
    if tp == "f":
        return (temp * 1.8) + 32
    elif tp == "c":
        return (temp - 32) / 1.8
    
def main():
    while True:
        try:
            tp = input("원하는 타입을 입력해주세요. 화씨로 변환하고 싶으면 f를, 섭씨로 변환하고 싶으면 c를 입력해주세요.: ")
            temp = float(input("온도를 입력해주세요.: "))

            if tp == "f":
                print(f"{temp}f => {trans_temp(tp, temp):.1f}c")
            else:
                print(f"{temp}c => {trans_temp(tp, temp):.1f}f")
            
            break

        except:
            print("타입을 잘못 입력하셨습니다. f와 c중 하나를 입력해주세요.")

if __name__ == "__main__":
    main()

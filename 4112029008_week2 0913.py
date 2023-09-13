def greet(name):
    return f"你好, {name}!"

def calculate_area(radius):
    """這個函數接收一個半徑值作為參數，然後返回圓的面積"""
    pi = 3.14159
    return pi * radius ** 2


def main():
     # 輸入和輸出
    name = input("請輸入你的名字")
    print(greet(name))

    for i in range(3):
        while True:
            # 資料類型和變量
            radius_str = input(f"請輸入圓的半徑（您還有{3-i}次機會）：")
            
            if radius_str.lower() == '退出':#為甚麼要.lower(轉換大小寫，但中文可以不用)
                print("感謝使用，再見！")
                return

            radius = float(radius_str)
            # 條件判斷
            if radius > 0:
                area = calculate_area(radius)
                print(f"圓的面積是：{area}")
                break
            else:
                print("半徑不能是負數或零！請再試一次。")
 
if __name__ == "__main__":#為甚麼要寫這句(如果有不只一個python檔，就必須要寫這句。 但這裡只有一個所以可以不用)
    main()


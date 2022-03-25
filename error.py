def split_bill(price):
    num = input("何人いで割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("正しい値を入力してください")
        print(e)
    except ValueError:
        print("数字を入力してください")
    else:
        print(f"一人{each}円です")
    finally:
        print("ご利用ありがとうございました。")


if __name__ == "__main__":
    split_bill(10000)
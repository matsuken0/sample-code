print("1:グー　2:チョキ　3:パー")
taro = int(input("太郎　1,2,3を入力:"))
hamako = int(input("花子　1,2,3を入力:"))
janken = ["あいこ","太郎 win", "花子 win"]

def janken_c(taro, hamako, c="c"):
    taro -= 1
    hamako -= 1

    if taro == hamako:
        print(f"janken_{c} あいこ")
    elif (taro + 1) % 3 == hamako:
        print(f"janken_{c} 太郎 win")
    else:
        print(f"janken_{c} 花子win")


def janken_b(t, h, b="b"):
    if t == h:
        print(f"janken_{b} あいこ")
    elif (t ==1 and h == 2) or (t ==2 and h == 3) or (t ==3 and h == 1):
        print(f"janken_{b} 太郎 win")
    else:
        print(f"janken_{b} 花子win")

def janken_d(taro, hamako, c="d"):
    taro -= 1
    hamako -= 1

    if taro == hamako:
        return 0, f"{c}"
    elif (taro + 1) % 3 == hamako:
        return 1, f"{c}"
    else:
        return 2, f"{c}"


# janken_c(taro, hamako)
j_d =janken_d(taro, hamako, "j_d")
print(f"func ({j_d[1]}) の結果は {janken[j_d[0]]}")

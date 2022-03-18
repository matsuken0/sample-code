class Janken:
    def __init__(self, name1="太郎", name2="花子"):
        self.name1 = name1
        self.name2 = name2
        kye = {1:"グー", 2:"チョキ", 3:"パー"}
        print(kye)
        self.taro = int(input(f"{name1}　1,2,3を入力:"))
        self.hanako = int(input(f"{name2}　1,2,3を入力:"))
        self.result = f"{self.name1}は{kye[self.taro]}、{self.name2}は{kye[self.hanako]}で"

    def janken_a(self):
        if self.taro == 1:
            if self.hanako == 1:
                print(f"{self.result} あいこ")
            elif self.hanako == 2:
                print(f"{self.result} {self.name1} win")
            else:
                print(f"{self.result} {self.name2} win")
        elif self.taro == 2:
            if self.hanako == 1:
                print(f"{self.result} {self.name2} win")
            elif self.hanako == 2:
                print(f"{self.result} あいこ")
            else:
                print(f"{self.result} {self.name1} win")
        else:
            if self.hanako == 1:
                print(f"{self.result} {self.name1} win")
            elif self.hanako == 2:
                print(f"{self.result} {self.name2} win")
            else:
                print(f"{self.result} あいこ")

    def janken_b(self):
        if self.taro == self.hanako:
            print(f"{self.result} あいこ")
        elif (self.taro ==1 and self.hanako == 2) or (self.taro ==2 and self.hanako == 3) or (self.taro ==3 and self.hanako == 1):
            print(f"{self.result} {self.name1} win")
        else:
            print(f"{self.result} {self.name2} win")

    def janken_c(self):
        self.taro -= 1
        self.hanako -= 1
        if self.taro == self.hanako:
            print(f"{self.result} あいこ")
        elif (self.taro + 1) % 3 == self.hanako:
            print(f"{self.result} {self.name1} win")
        else:
            print(f"{self.result} {self.name2} win")

    def janken_d(self):
        self.taro -= 1
        self.hanako -= 1
        janken_list = ["あいこ", f"{self.name1} win", f"{self.name2} win"]
        if self.taro == self.hanako:
            return self.result, janken_list[0]
        elif (self.taro + 1) % 3 == self.hanako:
            return self.result, janken_list[1]
        else:
            return self.result, janken_list[2]


class Person(Janken):
    def __init__(self, name1="太郎", name2="花子"):
        self.name1 = input("プレーヤー１を入力してください:")
        self.name2 = input("プレーヤー2を入力してください:")
        kye = {1:"グー", 2:"チョキ", 3:"パー"}
        print(kye)
        self.taro = int(input(f"{self.name1}　1,2,3を入力:"))
        self.hanako = int(input(f"{self.name2}　1,2,3を入力:"))
        self.result = f"{self.name1}は{kye[self.taro]}、{self.name2}は{kye[self.hanako]}で"
    pass


#ローカルリポ
if __name__ == "__main__":
    #janken_aからc
    janken_base = Janken()
    janken_base.janken_a()

    #janken_b専用
    # janken_base = Janken()
    # result, name = janken_base.janken_d()
    # print(result, name)

    #プレーヤーの名前入力
    # janken_base = Person()
    # janken_base.janken_a()
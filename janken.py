class Janken:
    def __init__(self, name1="太郎", name2="花子"):
        self.name1 = name1
        self.name2 = name2
        kye = {1:"グー", 2:"チョキ", 3:"パー"}
        print(kye)
        self.taro = int(input(f"{name1}　1,2,3を入力:"))
        self.hanako = int(input(f"{name2}　1,2,3を入力:"))
        self.result = f"{self.name1}は{kye[self.taro]}、{self.name2}は{kye[self.hanako]}で"


    def janken_c(self):
        self.taro -= 1
        self.hanako -= 1

        if self.taro == self.hanako:
            print(f"{self.result} あいこ")
        elif (self.taro + 1) % 3 == self.hanako:
            print(f"{self.result} {self.name1} win")
        else:
            print(f"{self.result} {self.name2} win")


    def janken_b(self):
        if self.taro == self.hanako:
            print(f"{self.result} あいこ")
        elif (self.taro ==1 and self.hanako == 2) or (self.taro ==2 and self.hanako == 3) or (self.taro ==3 and self.hanako == 1):
            print(f"{self.result} {self.name1} win")
        else:
            print(f"{self.result} {self.name2} win")

    def janken_d(self):
        self.taro -= 1
        self.hanako -= 1

        if self.taro == self.hanako:
            return 0
        elif (self.taro + 1) % 3 == self.hanako:
            return 1
        else:
            return 2




janken_base = Janken()
janken_c = janken_base.janken_c
janken_b = janken_base.janken_b
janken_b()

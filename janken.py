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
        print("A")
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
        print("B")
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

def input_name(func):
    def inner(*args):
        print("名前を入力してください")
        name1 = input("プレーヤー1を入力：")
        name2 = input("プレーヤー2を入力：")
        type = input("タイプ入力 a,b,c,d:")
        func(name1,name2,type)
    return inner

@input_name
def make_name(name1, name2, type):
    janken_base = Janken(name1, name2)
    janken_pattern = {"a":"janken_a", "b":"janken_b", "c":"janken_c", "d":"janken_d"}
    a = janken_pattern[type]
    print(a)
    janken_base.a()

make_name()

# janken_base = Janken()
# janken_base.janken_a()

# result, name = janken_base.janken_d()
# print(result, name)

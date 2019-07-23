class doscoresum:
    def __init__(self):
        get = input().split(', ')
        self.ko = int(get[0])
        self.en = int(get[1])
        self.ma = int(get[2])
        self.sumscore = self.ko + self.en + self.ma
        print(f"국어, 영어, 수학의 총점: {self.sumscore}")
        

this = doscoresum()
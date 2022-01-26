
class putin:
    def __init__(self,data):
        self.data = data
        self.data = self.data.splitlines()
        for x,y in enumerate(self.data):
            self.data[x] = list(y.split())
        print(self.data)


c = putin('''10 13
0 2 1
0 4 1
0 6 1
0 8 1
1 2 1
2 3 1
3 4 1
4 5 1
5 6 1
6 7 1
7 8 1
8 1 1
8 9 1''')
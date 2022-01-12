from abc import ABC, abstractmethod


class Digit:
    numbers_visual = {"0": "1111110", "1": "0110000", "2": "1101101", "3": "1111001", "4": "0110011", "5": "1011011", "6": "1011111",
                      "7": "1110000", "8": "1111111", "9": "1111011", "A": "1110111", "B": "0011111", "C": "1001110", "D": "0111101", "E": "1001111", "F": "1000111"}

    def __init__(self, num):
        self.num = num.upper()
        self.valid = self.is_valid(num)
        self.visual = self.numbers_visual[self.num]

    def is_valid(self, num):
        if num in self.numbers_visual:
            return True
        else:
            return False

    def get_visual(self):
        return self.visual


class Font(ABC):
    def __init__(self, font):
        self.visual_font1 = [[
            "111000000000000",
            "001001001000000",
            "000000001001001",
            "000000000000111",
            "000000100100100",
            "100100100000000",
            "000000111000000"], 3]
        self.visual_font2 = [[
            "0110000000000000000000000000",
            "0000000100010000000000000000",
            "0000000000000000000100010000",
            "0000000000000000000000000110",
            "0000000000000000100010000000",
            "0000100010000000000000000000",
            "0000000000000110000000000000"], 4]
        if font == "1":
            self.font = self.visual_font1
        elif font == "2":
            self.font = self.visual_font2

    def get_visual(self):
        return self.font


class Number:
    def __init__(self, numbers):
        self.font = Font("1")
        self.font = self.font.get_visual()
        self.visual_graph = []
        self.valid = True
        self.numbers = numbers
        self.numbers_list = list(self.numbers)
        self.visual_list = []
        for letter in self.numbers_list:
            visual = Digit(letter)
            if self.is_valid(visual):
                self.visual_list.append(visual)

    def is_valid(self, visual):
        if visual == "number is not valid":
            self.valid = False
            return False
        else:
            return True

    def visualize(self):
        if self.valid:
            big_whole = []
            bigger_whole = []
            for num in self.visual_list:
                current_font = [self.font[0][x] for x, y in enumerate(
                    [a for a in num.get_visual()]) if y == "1"]
                f = [max(k) for k in zip(*current_font)]
                whole = []
                row = []
                for x, y in enumerate(f):
                    if x % self.font[1] == 0:
                        if row != []:
                            whole.append(row)
                        row = []
                        row.append("●" if y == "1" else " ")
                    else:
                        row.append("●" if y == "1" else " ")
                whole.append(row)
                big_whole.append(whole)
            self.biggest_whole = []
            for row in range(len(big_whole[0])):
                big_row = []
                for letter in big_whole:
                    big_row.append(letter[row])
                self.biggest_whole.append(big_row)
            return self.biggest_whole


class Strokes:
    numbers_visual = {"0": "1111110", "1": "0110000", "2": "1101101", "3": "1111001", "4": "0110011", "5": "1011011", "6": "1011111",
                      "7": "1110000", "8": "1111111", "9": "1111011", "A": "1110111", "B": "0011111", "C": "1001110", "D": "0111101", "E": "1001111", "F": "1000111"}

    def __init__(self, num1, num2):
        self.num1 = num1.upper()
        self.num2 = num2.upper()
        self.num1_visual = self.numbers_visual[num1]
        self.num2_visual = self.numbers_visual[num2]

    def compare(self):
        actions = [["add", 0], ["remove", 0]]
        add = []
        remove = []
        for i in range(len(self.num1_visual)):
            if self.num1_visual[i] < self.num2_visual[i]:
                actions[0][1] += 1
                add.append(i)
            elif self.num1_visual[i] > self.num2_visual[i]:
                actions[1][1] += 1
                remove.append(i)
        return add, remove

    def move(self, actions):
        if actions[0][1] > actions[1][1]:
            actions[0][1] -= actions[1][1]
            actions[1][0] = "move"
        elif actions[0][1] < actions[1][1]:
            actions[1][1] -= actions[1][1]
            actions[0][0] = "move"
        return actions


#all_num = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
'''
all_num = ["1","2","3","4"]

whole = [all_num]
for x in all_num:
    column = []
    for y in all_num:
        cl = Strokes(x,y)
        column.append(cl.compare())
    whole.append([x,column])

for row in whole:
    print(row)
'''
c = Strokes("1", "2")
print(c.compare())
'''
c = Number("5345")
a = list(c.visualize())
for i in a:
    whole = []
    for x in i:
        whole.append("".join(x))
    print("    ".join(whole))
    '''

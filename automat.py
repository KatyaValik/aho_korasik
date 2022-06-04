from vertex import Vertex


class Automat:
    def __init__(self, words):
        self.words = self.low_words(words)
        self.k = 33
        self.vertex = [Vertex()]
        self.alphabet = self.get_alphabet()
        self.vertex[0].next = [-1 for i in range(0, self.k)]
        self.vertex[0].go = [-1 for i in range(0, self.k)]
        self.vertex[0].parent = -1
        self.vertex[0].link = -1
        self.vertex[0].text = ''
        self.size = 1
        self.final_v = []

    def add_word(self, word):
        v = 0
        for i in range(0, len(word)):
            c = ord(word[i]) - ord('а')
            if self.vertex[v].next[c] == -1:
                self.vertex.append(Vertex())
                self.vertex[self.size].next = [-1 for i in range(0, self.k)]
                self.vertex[self.size].go = [-1 for i in range(0, self.k)]
                self.vertex[self.size].link = -1
                self.vertex[self.size].parent = v
                self.vertex[self.size].pch = c
                self.vertex[v].next[c] = self.size
                self.vertex[self.size].text = self.vertex[v].text + word[i]
                self.size += 1
            v = self.vertex[v].next[c]
        self.vertex[v].leaf = True
        self.final_v.append(v)

    def create_auto(self):
        for word in self.words:
            self.add_word(word)
        self.find_all_links()

    def count_letters(self):
        s = set()
        for word in self.words:
            for i in range(0, len(word)):
                s.add(word[i])
        return len(s)

    def low_words(self, words):
        words_low = []
        for word in words:
            words_low.append(word.lower())
        return words_low

    def get_link(self, v):
        if self.vertex[v].link == -1:
            if v == 0 or self.vertex[v].parent == 0:
                self.vertex[v].link = 0
            else:
                self.vertex[v].link = self.go(self.get_link(self.vertex[v].parent), self.vertex[v].pch)
        return self.vertex[v].link

    def go(self, v, c):
        if self.vertex[v].go[c] == -1:
            if self.vertex[v].next[c] != -1:
                self.vertex[v].go[c] = self.vertex[v].next[c]
            else:
                if v == 0:
                    self.vertex[v].go[c] = 0
                else:
                    self.vertex[v].go[c] = self.go(self.get_link(v), c)
        return self.vertex[v].go[c]

    def find_all_links(self):
        for i in range(0, self.size):
            if self.vertex[i].link == -1:
                self.get_link(i)

    def get_alphabet(self):
        s = set()
        for word in self.words:
            for i in range(0, len(word)):
                s.add(word[i])
        res = list(s)
        return res

    def get_table(self):
        row_count = len(self.vertex)
        column_count = len(self.alphabet) + 1
        d = dict()
        for i in range(1, len(self.alphabet) + 1):
            d[i] = self.alphabet[i - 1]
        table = []
        for i in range(row_count):
            row = []
            for j in range(column_count):
                if j == 0:
                    row.append(i)
                else:
                    symbol = ord(d[j]) - ord('а')
                    if self.vertex[i].go[symbol] != -1:
                        item = self.vertex[i].go[symbol]
                    else:
                        item = self.go(i, symbol)
                    row.append(item)
            table.append(row)
        return table

    def get_link_table(self):
        table = []
        for i in range(len(self.vertex)):
            row = [i]
            row.append(self.vertex[i].link)
            table.append(row)
        return table

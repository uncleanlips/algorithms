 class Stack():
    def __init__(self):
        self.items = []

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def Peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def getStack(self):
        return ' '.join(self.items)

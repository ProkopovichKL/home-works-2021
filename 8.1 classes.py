class Stack:
    def __init__(self):
        self.__sflou = []

    def set_in(self, *args):
        self.__sflou.extend(args)    # Использовал метод "extend", чтобы не заморачиваться 
                                     # с внесением элементов по отдельности. Хотя по идее
    def __iter__(self):              # стек наполняется последовательно по-одному через "append".
        return self

    def __next__(self):
        try:
            return self.__sflou.pop()
        except IndexError:
            raise StopIteration
            
first = Stack()
first.set_in(1,2,3,4,5,6,7)

for i in first:
    print(i)

class Queue:
    def __init__(self):
        self.__qflou = []

    def set_in(self, *args):
        self.__qflou.extend(args)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.__qflou.pop(0)
        except IndexError:
            raise StopIteration
            
second = Queue()
second.set_in(10,20,30,40,50,60,70)

for i in second:
    print(i)
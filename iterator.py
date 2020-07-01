# https://www.youtube.com/watch?v=-PklUOOz4n8
def iter_underhood():
    x = [1, 2, 3, 4]
    it = iter(x)
    print(it)

    while True:
        try:
            val = next(it)
        except StopIteration:
            break
        print(f"{val=}")


def desugared():
    x = [1, 2, 3, 4]
    it = x.__iter__()
    print(it)

    while True:
        try:
            val = it.__next__()
        except StopIteration:
            break
        print(f"{val=}")


class MyListIterator:
    def __init__(self, my_list, index=0):
        self.my_list = my_list
        self.index = index

    def __next__(self):
        if self.index < len(self.my_list.data):
            val = self.my_list.data[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

    def __iter__(self):
        return MyListIterator(self.my_list, self.index)


class MyList:
    def __init__(self, data):
        self.data = list(data)

    # the combination of __getitem__ and __len__ can provide iterable feature
    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    # def __iter__(self):
    #     return MyListIterator(self)


def my():
    my_list = MyList([1, 2, 3, 4])
    print(my_list)
    it = iter(my_list)
    print(it)
    for i in it:
        print(i)


if __name__ == "__main__":
    iter_underhood()
    desugared()
    my()

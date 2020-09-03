# https://www.youtube.com/watch?v=-PklUOOz4n8
from collections import abc
import types


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
        return self


class MyList:
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    # the __iter__ provide iterable feature
    def __iter__(self):
        return MyListIterator(self)


# use generator to implement iterable doesn't need a separate iterator
class MyListG:
    def __init__(self, data):
        self.data = list(data)

    # def __getitem__(self, index):
    #     return self.data[index]

    # def __len__(self):
    #     return len(self.data)

    def __iter__(self):
        for d in self.data:
            yield d
        return


def my():
    print(f"{issubclass(MyList, abc.Iterable)=}")
    my_list = MyList([1, 2, 3, 4])
    print(f"{isinstance(my_list, abc.Iterable)=}")
    print(my_list)
    it = iter(my_list)
    print(f"{isinstance(it, types.GeneratorType)=}")
    print(it)
    for i in it:
        print(i)

    print(f"{issubclass(MyListG, abc.Iterable)=}")
    my_list_g = MyListG(list(range(5, 10)))
    print(f"{isinstance(my_list_g, abc.Iterable)=}")
    it_g = iter(my_list_g)
    print(f"{isinstance(it_g, types.GeneratorType)=}")
    print(it_g)
    for i in it_g:
        print(i)


if __name__ == "__main__":
    iter_underhood()
    desugared()
    my()

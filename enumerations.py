from enum import Enum, unique


@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


if __name__ == "__main__":
    if 1 in [c.value for c in Color]:
        print("yeah")
    k = Color.RED
    print(f"{k=}")
    v = Color.RED.value
    print(f"{v=}")

import pytest
import matplotlib.pyplot as plt


def main():
    x = []
    y = []
    for i in range(-10, 10):
        if i == 0:
            continue
        x.append(i)
        y.append(func(i))
    plt.plot(x, y)
    plt.show()


def func(x):
    return 1 / (x * x)


if __name__ == "__main__":
    main()
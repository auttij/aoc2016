import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def get_drop_time(discs):
    time = 0

    while True:
        positions = [
            (time + val[0] + i) % val[1] for i, val in enumerate(discs, start=1)
        ]
        if sum(positions) == 0:
            return time
        time += 1


@timer
@print_result
def exercise1(arr):
    discs = [(pos, count) for _, count, _, pos in arr]
    return get_drop_time(discs)


@timer
@print_result
def exercise2(arr):
    discs = [(pos, count) for _, count, _, pos in arr]
    discs.append((0, 11))
    return get_drop_time(discs)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])

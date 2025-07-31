#!/usr/bin/env python3

global_counter = 0

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        global global_counter
        global_counter += 1
        self.count += 1

    def get_count(self):
        return self.count

    def get_global(self):
        return global_counter


def main():
    x = Counter()
    y = Counter()

    x.increment()
    x.increment()
    print(f'x count = {x.get_count()}')
    print(f'global count from x = {x.get_global()}')

    y.increment()
    print(f'y count = {y.get_count()}')
    print(f'global count from y = {y.get_global()}')

if __name__ == '__main__':
    main()

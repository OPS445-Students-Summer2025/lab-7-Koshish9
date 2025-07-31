#!/usr/bin/env python3

class MyCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


def main():
    c1 = MyCounter()
    c2 = MyCounter()

    c1.increment()
    c1.increment()
    print(f'c1 count = {c1.get_count()}')

    c2.increment()
    print(f'c2 count = {c2.get_count()}')

if __name__ == '__main__':
    main()

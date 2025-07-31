#!/usr/bin/env python3

global_counter = 0

class GlobalCounter:
    def increment(self):
        global global_counter
        global_counter += 1

    def get_count(self):
        return global_counter


def main():
    a = GlobalCounter()
    b = GlobalCounter()

    a.increment()
    a.increment()
    print(f'a count = {a.get_count()}')

    b.increment()
    print(f'b count = {b.get_count()}')

if __name__ == '__main__':
    main()

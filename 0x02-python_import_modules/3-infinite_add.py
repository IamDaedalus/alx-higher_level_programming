#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    def calc():
        """Adds every cmdline arg as a value and prints the result"""
        cur_arg = 0
        argc = len(sys.argv)

        if argc > 1:
            for arg in range(1, argc):
                cur_arg += int(sys.argv[arg])
        print(cur_arg)

    calc()

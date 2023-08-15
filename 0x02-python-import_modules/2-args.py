#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    def get_args():
        """Gets and prints every cmdline arg passed to the file"""
        argc = len(sys.argv)
        if argc == 1:
            print("0 arguments.")
        elif argc > 1:
            print("{} arguments:".format(argc - 1))
            for i in range(1, argc):
                print("{}: {}".format(i, sys.argv[i]))

    get_args()

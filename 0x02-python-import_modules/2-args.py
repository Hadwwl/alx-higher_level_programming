#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    rank = len(sys.argv) - 1
    if rank == 0:
        print("0 arguments.")
    elif rank == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(rank))
    for i in range(rank):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

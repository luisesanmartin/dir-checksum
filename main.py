import sys
import os
import utils

def main():

    try:
        root = os.path.abspath(sys.argv[1])
    except IndexError: # no path provided
        root = os.path.abspath('./')

    utils.dir_checksum(root)

    return True

if __name__ == '__main__':
    main()

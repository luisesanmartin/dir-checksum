import sys
import utils

ROOT = sys.argv[0]

def main():

    utils.dir_checksum(ROOT)

    return True

if __name__ == '__main__':
    main()

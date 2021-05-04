import json
import sys

from DiaScanner.scanner import Scanner


def scan(config=None):
    if config is None:
        device = input("Please enter the id of your scanning device (e.g. 0)")
        base_name = input("Please enter the basename for your images:")
        suffix = input("Please enter the suffix for your images:")
    else:
        with open(config, 'r') as c:
            # import the values into the variables (also this saves code the json key is ignored and only the order matters)
            device, base_name, suffix = json.load(c).values()
    sc = Scanner(int(device), base_name=base_name, suffix=suffix)
    sc.preview()


if __name__ == '__main__':
    path = None
    # if there is at least one commandline argument use the first as config path
    if len(sys.argv) > 1:
        path = sys.argv[1]
    scan(path)

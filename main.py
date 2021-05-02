from DiaScanner.scanner import Scanner


def scan():
    basename = input("Please enter the basename for your images:")
    suffix = input("Please enter the suffix for your images:")
    sc = Scanner(1, base_name=basename, suffix=suffix)
    sc.preview()


if __name__ == '__main__':
    scan()

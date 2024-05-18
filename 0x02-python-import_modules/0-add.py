#!/usr/bin/python3
def main():
    from add_0 import add
    if __name__ == '__main__':
        a = 1
        b = 2
        result = add(a, b)
        print("{0} + {1} = {2}".format(a, b, result))
if __name__ == '__main__':
    main()

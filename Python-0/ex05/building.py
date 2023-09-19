import sys


def building(str):
    """
    check what does a string contains
    """
    up, low, punc, space, digit = 0, 0, 0, 0, 0
    print(f"The text contains {len(str)} characters:")
    for s in str:
        if (s.isdigit()):
            digit += 1
        elif (s.isupper()):
            up += 1
        elif (s.islower()):
            low += 1
        elif (s.isspace()):
            space += 1
        elif (not s.isalnum() and not s.isspace()):
            punc += 1
    print(f"{up} upper letters")
    print(f"{low} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")
    pass


def main():
    """This is a main, By Odin, by Thor ! Use your brain !!!"""

    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
        if (len(sys.argv) < 2):
            str = input("What is the text to count?\n")
        else:
            str = sys.argv[1]
        building(str)
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except IndexError:
        pass
    except TypeError:
        pass
    except KeyboardInterrupt:
        pass


main()

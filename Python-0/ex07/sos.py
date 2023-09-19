import sys


def check_str(str):
    for c in str:
        if not (c.isalpha() or c.isdigit() or c == ' '):
            return False
    return True


def sos(str):
    print_str = ""
    MORSE_CODE = {
    ' ': '/ ','a': '.- ','b': '-... ','c': '-.-. ','d': '-.. ','e': '. ',
    'f': '..-. ','g': '--. ','h': '.... ','i': '.. ','j': '.--- ','k': '-.- ',
    'l': '.-.. ','m': '-- ','n': '-. ','o': '--- ','p': '.--. ','q': '--.- ',
    'r': '.-. ','s': '... ','t': '- ','u': '..- ','v': '...- ','w': '.-- ',
    'x': '-..- ','y': '-.-- ','z': '--.. ','1': '.---- ','2': '..--- ',
    '3': '...-- ','4': '....- ','5': '..... ','6': '-.... ','7': '--... ',
    '8': '---.. ','9': '----. ','0': '----- '}
    for c in str.lower():
        print_str = print_str + MORSE_CODE[c]
    print(print_str)


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad here"
        assert check_str(sys.argv[1]), "the arguments are bad here"
        sos(sys.argv[1])
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except ValueError:
        print("AssertionError: the arguments are bad here")
    except IndexError:
        print("AssertionError: the arguments are bad here")
    except TypeError:
        print("AssertionError: the arguments are bad here")
    except KeyboardInterrupt:
        pass


main()
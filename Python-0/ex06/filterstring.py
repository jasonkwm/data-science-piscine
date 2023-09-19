import sys
from ft_filter import ft_filter


def filterstring(str, word_len):
    """
    By Najib, by Anwar ! Use your brain !!!
    @param
    str = string will be split
    word_len = length of word to compare
    """
    word_split = str.split()
    return ft_filter(lambda a: len(a) > word_len, word_split)


def main():
    """This is a main, By Odin, by Thor ! Use your brain !!!"""
    try:
        assert len(sys.argv) < 4, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        word_len = int(sys.argv[2])
        print(filterstring(sys.argv[1], word_len))
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


if __name__ == "__main__":
    main()
